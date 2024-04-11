from django.db import models

class DatosPersonales(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    pais = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=20)
    numero = models.CharField(max_length=10)
    email = models.EmailField()