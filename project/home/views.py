from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from . import forms

def index(request):
    return render(request, "home/index.html")

def about(request):
    return render(request,"home/about.html")

def login_request (request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usurio = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user= authenticate(username=usurio, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "home/index.html" ,{"mensaje":f"se ha logeado correctamente."})
    else:
        form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})
