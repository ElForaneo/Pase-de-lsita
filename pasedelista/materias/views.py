from django.shortcuts import render
from django.views import View

# Create your views here.

class materias(View):
    def get(self, request):
     context={}
     return render(request, 'materias.html', context)