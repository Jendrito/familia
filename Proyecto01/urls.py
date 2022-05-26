"""Proyecto01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto01.views import saludo, despedida, diadeHoy, minombreEs, nacimiento, probandoTemplate
from familia.views import familia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name ='saludo'),
    path('despedida/', despedida, name = 'despedida'),
    path('diadeHoy/', diadeHoy, name = 'diadeHoy'),
    path('minombreEs/<nombre>/', minombreEs, name = 'minombre'),
    path('nacimiento/<cumpleaños>/', nacimiento, name = 'nacimiento'),
    path('probandoTemplate/', probandoTemplate, name = "probandoTemplate"),
    path('familia/', familia, name = 'familia'),
]

