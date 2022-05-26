from django.db import models

class Familia(models.Model):
    nombre = models.CharField(max_length=12)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    descripcion = models.CharField(max_length=200, blank=True, null=True)