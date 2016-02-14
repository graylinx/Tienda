#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, HttpResponseBadRequest
from django.views import generic
from itertools import chain 
# Create your views here.
from shop.models import Bicicletas, Canciones, Libros, Pedido
from shop.forms import PedidoForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core import serializers
import re


def index(request):
    bicicletas = Bicicletas.objects.all()[:4]
    canciones = Canciones.objects.all()[:4]
    libros = Libros.objects.all()[:4]
    context = {}
    result_list = list(chain(bicicletas, canciones, libros))
    context['result_list'] = result_list
    return render(request, 'shop/index.html', context)

def seccion(request, clase):
    if clase == "bicicletas":
      seccion = Bicicletas.objects.all()
    elif clase == "canciones":
      seccion = Canciones.objects.all()
    elif clase == "libros":
      seccion = Libros.objects.all()
    context = {}
    context['seccion'] = seccion
    return render(request, 'shop/seccion.html', context)

def producto(request, clase, id_producto):
    if clase == "bicicletas":
        producto = Bicicletas.objects.get(id=id_producto)
    elif clase == "canciones":
        producto = Canciones.objects.get(id=id_producto)
    elif clase == "libros":
        producto = Libros.objects.get(id=id_producto)
    context = {}
    context['producto'] = producto
    return render(request,'shop/producto.html', context)

def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = request.POST['username']
            clave = request.POST['password2']
            if request.COOKIES.has_key(str(request.user)):
                carrito = request.COOKIES[str(request.user)]
            else:
                carrito = ''
            acceso = authenticate(username=usuario, password=clave)
            login(request, acceso)
            cookies = HttpResponseRedirect('/shop/')
            cookies.set_cookie(str(request.user), carrito)
            return cookies
    else:
        formulario = UserCreationForm()
    return render(request, 'shop/usuario.html', {'formulario':formulario})

def ingresar (request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/shop/')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            if request.COOKIES.has_key(str(usuario)):
                carrito = request.COOKIES[str(usuario)]
            else:
                carrito = ''
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                login(request, acceso)
                cookies = HttpResponseRedirect('/shop/')
                cookies.set_cookie(str(request.user), carrito)
                return cookies
            else:
                return render(request, 'shop/nousuario.html')
    else:
        formulario = AuthenticationForm()
    return render(request,'shop/ingresar.html',{'formulario':formulario})

def logout_(request):
    logout(request)
    response = HttpResponseRedirect('/shop/')
    return response


def search_items(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        if len(search_text)>= 3:
            bicicletas = Bicicletas.objects.filter(nombre__contains=search_text)
            canciones = Canciones.objects.filter(nombre__contains=search_text)
            libros = Libros.objects.filter(nombre__contains=search_text)
            articles = list(chain(bicicletas, canciones, libros))
        else:
            bicicletas = Bicicletas.objects.none()
            canciones = Canciones.objects.none()
            libros = Libros.objects.none()
            articles = list(chain(bicicletas, canciones, libros))
    else:
        search_text = ''

    context = {}
    context['articles'] = articles
    return render(request, 'shop/ajax_search.html',context)

def carrito(request):
    bicicletas = Bicicletas.objects.all()
    canciones = Canciones.objects.all()
    libros = Libros.objects.all()
    context = {}
    final = []
    cookies_list = []
    precio = 0
    result_list = list(chain(bicicletas, canciones, libros))
    if request.COOKIES.has_key(str(request.user)):
        cookies_list = request.COOKIES[str(request.user)].split('-')
    for items in result_list:
        for cooks in cookies_list:
            if str(cooks) == str(items.ref):
                 final += [items]
                 precio += float(items.precio)
    context['final'] = final
    context['precio'] = precio

    if request.POST:
        form = PedidoForm(request.POST)
        if form.is_valid():
            nuevo_pedido = form.save(commit=False)
            nuevo_pedido.articulos = cookies_list
            nuevo_pedido.nombre = str(request.user)
            nuevo_pedido.save()
            return HttpResponseRedirect('/shop/pedido')
    else:
        form = PedidoForm()
    context['form'] = form
    return render(request, 'shop/carrito.html',context)

def pedido(request):
    num_pedido = Pedido.objects.latest('articulos')
    context = {}
    context['num_pedido'] = num_pedido
    response = render(request, 'shop/pedido.html', context)
    if request.COOKIES.has_key(str(request.user)):
        response.delete_cookie(str(request.user))
    return response

