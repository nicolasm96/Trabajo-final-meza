from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login



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

def registro(request):
    if request.method == "POST":

        form = UserCreationForm(request.POST)
        if form.is_valid():

                username = form.cleaned_data["username"]
                form.save()
                return render(request,"home/index.html", {"mensaje":f"se ha registrado correctamente."})   
    else:
        form = UserCreationForm ()
        return render(request,"home/registro.html", {"form" : form})
            

