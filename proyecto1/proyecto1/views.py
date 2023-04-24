from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader

def saludar(request):
    return HttpResponse("Hola Mundo!")

def segunda_vista(request):
    return HttpResponse("Ya entendi!")

def dia_de_hoy(request):
    dia = datetime.datetime.today()
    cadena = (f"Hoy es {dia}")
    return HttpResponse(cadena)

def saludo_con_nombreytodo(request, nombre):
    return HttpResponse(f"Hola {nombre}, que hay?")

def calcula_anio_nacimiento(request, edad):
    actual = datetime.datetime.today().year
    nacimiento = actual - int(edad)
    return HttpResponse(f"Naciste en el año {nacimiento}")

"""def probando_html(request):
    diccionario = {"nombre":"Mike", "apellido":"Sirola", "edad":20, "lista":[10,5,2,7,8,3,8,10]}

    archivo = open(r"/home/mike/Desktop/PrimerDjango/Plantillas/template1.html")

    texto = archivo.read()
    archivo.close()

    template = Template(texto)
    contexto = Context(diccionario)
    documento = template.render(contexto)
    return HttpResponse(documento)"""

def probando_html(request):

    diccionario = {"nombre":"Mike", "apellido":"Sirola", "edad":20, "lista":[10,5,2,7,8,3,8,10]}

    template=loader.get_template("template1.html")
    documento=template.render(diccionario)
    return HttpResponse(documento)
