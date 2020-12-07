from django import forms
from clases.models import Hora, Clase

class Clasesforms(forms.ModelForm):
    class Meta:
        model = Clase
        field = '__all__'
        exclude = []