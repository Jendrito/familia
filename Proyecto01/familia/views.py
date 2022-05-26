from django.shortcuts import render
from familia.models import Familia

# Create your views here.

def familia(request):
    miembrofamilia_01 = Familia.objects.create(
        nombre = "Alejandra",
        edad = 44,
        nacimiento = "1977-07-17",
        descripcion = "Madre, diseñadora gráfica")
    miembrofamilia_02 = Familia.objects.create(
        nombre = "Esteban",
        edad = 32,
        nacimiento = "1989-09-06",
        descripcion = "Padre, operador de radio")
    miembrofamilia_03 = Familia.objects.create(
        nombre = "Miranda",
        edad = 17,
        nacimiento = "2005-06-15",
        descripcion = "Hija mayor, estudiante secundaria")
    miembrofamilia_04 = Familia.objects.create(
        nombre = "Antonia",
        edad = 11,
        nacimiento = "2011-02-04",
        descripcion = "Hija menor, estudiante primaria")
    context = {"miembrofamilia_01":miembrofamilia_01, 
            "miembrofamilia_02":miembrofamilia_02,
            "miembrofamilia_03":miembrofamilia_03,
            "miembrofamilia_04":miembrofamilia_04}
    return render(request,'familia.html',context=context)