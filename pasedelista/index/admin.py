from django.contrib import admin
from .models import Alumno, Asistencia, Profesore

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Asistencia)
admin.site.register(Profesore)