from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Auto

def inicio(request):
    return HttpResponse('<h1>SOY EL INICIO</h1>')

def saludo(request, nombre, apellido):
    fecha = datetime.now()
    return HttpResponse(f'<h1>{fecha.strftime('%H:%M:%S')}: Hola {nombre} {apellido}</h1>')

def saludo_template(request, nombre, apellido):
    
    # with open(r'C:\Users\cdbia\Desktop\76395\dj76395\templates\saludo_template.html') as archivo_abierto:
    #     ...
    
    # archivo_abierto = open(r'C:\Users\cdbia\Desktop\76395\dj76395\templates\saludo_template.html') # ruta absoluta
    archivo_abierto = open(r'templates\saludo_template.html') # ruta relativa
    template = Template(archivo_abierto.read())
    archivo_abierto.close()
    
    
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha.strftime('%H:%M:%S'),
        'nombre': nombre,
        'apellido': apellido,
    }
    
    contexto = Context(datos)
    
    template_renderizaro = template.render(contexto)
    
    return HttpResponse(template_renderizaro)


def saludo_con_cargador(request, nombre, apellido):
    
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha.strftime('%H:%M:%S'),
        'nombre': nombre,
        'apellido': apellido,
    }
    
    
    # archivo_abierto = open(r'templates\saludo_template.html') # ruta relativa
    # template = Template(archivo_abierto.read())
    # archivo_abierto.close()
    
    template = loader.get_template(r'saludo_template.html')
    
    # contexto = Context(datos)
    
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)


def saludo_con_render(request, nombre, apellido):
    
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha.strftime('%H:%M:%S'),
        'nombre': nombre,
        'apellido': apellido,
    }
    

    # template = loader.get_template(r'saludo_template.html')
    
    # template_renderizado = template.render(datos)
    
    # return HttpResponse(template_renderizado)

    return render(request, 'inicio/saludo_template.html', datos)

def condicion_y_bucle(request):
    
    return render(request, 'subcarpeta/condicion_y_bucle.html', {
        "listado_de_numeros": [1,2,3,4,5,1,2,4,1,23,54,2,2,2,5,2,4,6,4,6,4,9,6,8,6,8,6,4,4]
    })
    
def crear_auto(request, marca, modelo):
    
    auto = Auto(marca=marca, modelo=modelo)
    
    auto.save()
    
    return render(request, 'inicio/crear_auto.html', {'auto': auto})