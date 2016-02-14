from django.db import models
from django.forms import ModelForm

# Create your models here.

class Bicicletas(models.Model):
    clase = "bicicletas"
    nombre = models.CharField(max_length=50)
    ref = models.IntegerField()
    tipo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='photos', blank=True, verbose_name='photos')
    video = models.FileField(upload_to="videos", blank= True, verbose_name='video')
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=7, decimal_places=2)

    def __unicode__(self):              # __unicode__ on Python 2
            return self.nombre



class Libros(models.Model):
    clase = "libros"
    nombre = models.CharField(max_length=50)
    ref = models.IntegerField()
    tipo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='photos', blank=True, verbose_name='picture')
    video = models.FileField(upload_to="videos", blank= True, verbose_name='video')
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=7, decimal_places=2)

    def __unicode__(self):              # __unicode__ on Python 2
            return self.nombre

class Canciones(models.Model):
    clase = "canciones"
    nombre = models.CharField(max_length=50)
    ref = models.IntegerField()
    tipo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='photos', blank=True, verbose_name='picture')
    video = models.FileField(upload_to="videos", blank= True, verbose_name='video')
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=7, decimal_places=2)

    def __unicode__(self):              # __unicode__ on Python 2
            return self.nombre

class Pedido(models.Model):
    nombre = models.CharField(max_length=50)
    articulos =models.CharField(max_length=100)
    correo = models.EmailField()
    numero = models.CharField(max_length=9)

    def __unicode__(self):
        return 'Pedido %i , de %s' %(self.id, self.nombre)


