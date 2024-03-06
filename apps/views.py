from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona

from django.contrib.auth.decorators import  login_required


# Create your views here.


def base(request):
    return render(request,"base.html")
def bienvenido(request):
    personas = Persona.objects.all()
    return render(request, 'bienvenido.html',{'personas':personas})# Renderiza la plantilla 'bienvenido.html' y devuelve la respuesta HTML al usuario


def inicio(request):
    return render(request,'inicio.html')

@login_required
def contenido(request):
    return render(request, "contenido.html")







