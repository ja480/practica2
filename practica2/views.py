#from multiprocessing import context
#from re import template
from mmap import mmap
from urllib.request import HTTPErrorProcessor
from django.http import HttpResponse
from django.template import loader
import datetime
from django.template import Template, Context
from django.shortcuts import render
class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
def saludo(request):
    #documento = "<html><body><h1>hola mundo</h1></body></html>"
    P1 = Persona("Maria", "Perez")
    ahora=datetime.datetime.now()
    #doc_externo = open("C:/Users/jafeth/Documents/Django/practica2/practica2/miplantilla.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    doc_externo=loader.get_template('miplantilla.html')
    temas_curso=["Plantillas", "Modelos", "Formularios", "Vistas"]
    ctx=Context({"nombre_persona":P1.nombre, "apellido_persona":P1.apellido, "hoy":ahora, "temas":temas_curso})
    #nombre = "Juan"
    #apellido = "Mendoza"
    #ctx=Context({"nombre_persona":nombre, "apellido_persona":apellido})
    #documento=plt.render(ctx)
    documento = doc_externo.render({"nombre_persona":P1.nombre, "apellido_persona":P1.apellido, "hoy":ahora, "temas":temas_curso})
    #return render(request, "miplantilla.html", {"nombre_persona":P1.nombre, "apellido_persona":P1.apellido, "hoy":ahora, "temas":temas_curso})
    return render(request, "miplantilla.html", {"nombre_persona":P1.nombre, "apellido_persona":P1.apellido, "hoy":ahora, "temas":temas_curso})
    #return(HttpResponse("Hola mundo"))
    #Hola

def despedida(request):
    documento = "<html><body><h1>Adios</h1></body></html>"
    return(HttpResponse(documento))

def damefecha(request):
    fecha_actual=datetime.datetime.now()
    documento = """<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>"""%fecha_actual
    return(HttpResponse(documento))

def calcular_edad(request, anio):
    edad_actual = 18
    periodo=anio
    edad_futura = edad_actual + periodo
    documento = """
    <html>
    <body>
    <h1>
    En el año %s tendras %s años
    </h1>
    </body>
    </html>
    """ %(anio, edad_futura)
    return(HttpResponse(documento))

def calcular_edad2(request, anio, edad_actual):
    #edad_actual = 18
    periodo=anio
    edad_futura = edad_actual + periodo
    documento = """
    <html>
    <body>
    <h1>
    En el año %s tendras %s años
    </h1>
    </body>
    </html>
    """ %(anio, edad_futura)
    return(HttpResponse(documento))

def producto1(request):
    return render(request, 'producto1.html')

def cabecera(request):
    return render(request, 'cabecera/barra.html')

def index(request):
    return render(request, 'index.html')
