from django import forms
from clases.models import Hora, Clase
from materias.models import Materia

class Clasesforms(forms.ModelForm):
    class Meta:
        model = Clase
        field = '__all__'
        exclude = []

class Materiaforms(forms.ModelForm):
    class Meta:
        model = Materia
        field = '__all__'
        exclude = []