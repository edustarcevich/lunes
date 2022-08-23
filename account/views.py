

from django.shortcuts import render, redirect


#################################################
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForms, UserCreationForm

# Create your views here.


def Login_view (request):
    print ("inciando sesion")

    form = LoginForms ()
    if request.method == "POST":
        form =LoginForms (request.POST)
        if form.is_valid():
            user = authenticate (
                username = form.cleaned_data.get ("username"),
                password = form.cleaned_data.get ("password")
           )
            if user is not None:
                login (request, user)
                return redirect ("home")
                
            else:
                messages.info (request, "credenciales invalidas")
        else:
            messages.error (request, "hay un errores en el formulario")
    return render (request,"account/login.html",context={"form":form})
    


def Logout_view (request):

    logout (request)
    print ("cerrando sesion")
    return redirect ("login")


def Register_view (request):
    form = UserCreationForm ()
    if request.method == "Post":
        form = UserCreationForm (request.POST)
        if form.is_valid ():
            return redirect ("home")
    return render (request, "account/register_user.html", {"form":form})