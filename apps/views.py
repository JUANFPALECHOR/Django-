from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona


# Create your views here.

def bienvenido(request):
    personas = Persona.objects.all()
    return render(request, 'bienvenido.html',{'personas':personas})# Renderiza la plantilla 'bienvenido.html' y devuelve la respuesta HTML al usuario

def casa(request):
    return render(request,'casa.html')

def despedida(request):
    return render(request,"base.html")


def contenido(request):
    return render(request, "contenido.html")





