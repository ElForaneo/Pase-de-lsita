from django.db import models


# Create your models here.

class Hora(models.Model):
    Hora = models.CharField(max_length=50)

class Clase(models.Model):
    Fecha = models.CharField(max_length=50)
    hora = models.ForeignKey(Hora, on_delete=models.CASCADE)

    def __str__ (self):
        return self.Fecha

