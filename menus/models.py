from django.db import models
import datetime

class Menu(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField('date published')
    def __str__(self):
        return self.titulo    

class Plato(models.Model):
    menu = models.ForeignKey(Menu)
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200,blank=True)
    tipo = models.CharField(max_length=20)
    def __str__(self):
        return self.titulo

class Excepcion(models.Model):
    plato = models.ForeignKey(Plato)
    descripcion = models.CharField(max_length=500)
    def __str__(self):
        return self.descripcion