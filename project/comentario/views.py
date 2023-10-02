from django.shortcuts import render, redirect
from .models import Comentario
from .forms import ComentarioForm

def index(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comentario:exito_comentario')
    else:
        form = ComentarioForm()
    
    comentarios = Comentario.objects.all()
    
    return render(request, 'comentario/index.html', {'form': form, 'comentarios': comentarios})

def exito_comentario(request):
    return render(request, 'comentario/exito_comentario.html')


# Create your views here.
