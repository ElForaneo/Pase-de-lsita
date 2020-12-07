from django.db import models

# Create your models here.


class Materia(models.Model):
    nombre = models.CharField(max_length=15)
    periodo = models.CharField(max_length=10)
    año = models.IntegerField(default=2020)
    id_clase = models.ForeignKey('clases.Clase', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre