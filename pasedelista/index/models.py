from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Profesore(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=15)
    id_materias = models.ForeignKey('materias.Materia', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Asistencia(models.Model):
    id_clase = models.ForeignKey('clases.Clase', on_delete=models.CASCADE)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    tiempo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_clase