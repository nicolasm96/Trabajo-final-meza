
from django.shortcuts import render,redirect
from . import models
from . import forms

def index(request):
     clientes = models.Cliente.objects.all()

     return render(request,"cliente/index.html", {"clientes": clientes})

def crear(request):
     if request.method == "POST":
          form = forms.clienteForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect("cliente:index")
     else:
          form = forms.clienteForm()
     return render(request, "cliente/crear.html",{"form":form})


# Create your views here.
