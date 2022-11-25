"""practica2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from practica2.views import index

from practica2.views import saludo, despedida, damefecha, calcular_edad, calcular_edad2, producto1, index, cabecera

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('saludo/', saludo),
    path('adios/', despedida),
    path('fecha/', damefecha),
    path('edades/<int:anio>/', calcular_edad),
    path('edades2/<int:edad_actual>/<int:anio>', calcular_edad2),
    path('producto/', producto1),
    path('cabecera/', cabecera),
    #path('edades/<int anio>/', calcular_edad),
]
