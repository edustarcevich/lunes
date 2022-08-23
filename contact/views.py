from django.shortcuts import render

# Create your views here.

def Contacto (request):
    return render (request, "contact/contacto.html", context={})