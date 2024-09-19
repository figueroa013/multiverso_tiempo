from django.db import models


class EventoNoCanonico(models.Model):
    año = models.IntegerField()
    nombre = models.CharField(max_length=215)
    imagen1 = models.CharField(max_length=215, default="default_image.jpg")
    imagen2 = models.CharField(max_length=215, default="default_image.jpg")
    descripcion = models.TextField()