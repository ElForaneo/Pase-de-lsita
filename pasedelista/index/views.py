from django.shortcuts import render, redirect
from django.views import View
from clases.models import Clase , Hora
from .forms import Clasesforms

# Create your views here.

class home(View):
    def get(self, request):

        clases = Clase.objects.all()
        for clas in clases:
            print(clas)
        
        context={'clases': clases }
        return render(request, 'index.html', context)

class clasesadd(View):
    def get(self,request):
        form = Clasesforms()
        context = {'form':form}
        return render(request, 'clasesadd.html', context)

    def post(self,request):
        form = Clasesforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = Clasesforms()
            context = {'form':form}
            return render(request, 'clasesadd.html', context)

class clasesUpdate(View):
    def get(self,request,id):
        clase = Clase.objects.get(id=id)
        form = Clasesforms(instance = clase)
        context = {'form': form}
        return render(request, 'clasesadd.html',context)

    def post(self,request, id):
        clase = Clase.objects.get(id=id)
        form = Clasesforms(request.POST, instance = clase)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = Clasesforms()
            context = {'form':form}
            return render(request, 'clasesadd.html', context)
