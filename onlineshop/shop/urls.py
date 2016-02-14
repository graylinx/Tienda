#encoding:utf-8
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from shop import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^(bicicletas|canciones|libros)/$', views.seccion),
    url(r'^(bicicletas|canciones|libros)/(\d+)/$', views.producto),
    url(r'^usuario_nuevo/$', views.nuevo_usuario),
    url(r'^ingresar/$', views.ingresar),
    url(r'^logout/$', views.logout_),
    url(r'^search/$', views.search_items),
    url(r'^carrito/$', views.carrito),
    url(r'^pedido/$',views.pedido),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
