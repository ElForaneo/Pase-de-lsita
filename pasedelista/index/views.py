from django.shortcuts import render, redirect
from django.views import View
from clases.models import Clase , Hora
from .forms import Clasesforms
from materias.models import Materia
from .forms import Materiaforms

# Create your views here.

class home(View):
    def get(self, request):

        clases = Clase.objects.all()
        materias = Materia.objects.all()
        for clas in clases:
            print(clas)

        context={'clases': clases,
                'materias':materias
         }
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

class materiaadd(View):
    def get(self,request):
        form = Materiaforms()
        context = {'form':form}
        return render(request, 'materiaadd.html', context)

    def post(self,request):
        form = Materiaforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = Materiaforms()
            context = {'form':form}
            return render(request, 'materiaadd.html', context)

class materiaUpdate(View):
    def get(self,request,id):
        materia = Materia.objects.get(id=id)
        form = Materiaforms(instance = materia)
        context = {'form':form} 
        return render(request, 'materiaadd.html', context)

    def post(self,request,id):
        materia = Materia.objects.get(id=id)
        form = Materiaforms(request.POST, instance = materia)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = Materiaforms()
            context = {'form':form}
            return render(request, 'materiaadd.html', context)