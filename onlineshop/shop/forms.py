from django.forms import ModelForm
from django import forms
from shop.models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ('articulos', 'nombre')
        field = ('correo', 'numero')
