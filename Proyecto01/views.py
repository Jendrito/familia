from re import M
from django.http import HttpResponse

from datetime import datetime

from django.shortcuts import render

def saludo(request):
    return HttpResponse("¡Hola!")

def despedida(request):
    return HttpResponse("¡Chau!")

def diadeHoy(request):
    dia = datetime.now()
    mensaje = f"Hoy es {dia}"
    return HttpResponse(mensaje)

def minombreEs(request, nombre):
    return HttpResponse(f"Mi nombre es {nombre}")

def nacimiento(request, cumpleaños):
    cumpleaños = int(cumpleaños)
    return HttpResponse(f"Naciste hace {2022 - cumpleaños} años")

def probandoTemplate(request):
    context = {
        'edades': [5, 10, 15, 20,]

    }
    return render(request, 'template1.html', context = context)