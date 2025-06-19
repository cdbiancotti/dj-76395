from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context


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
    
    
    archivo_abierto = open(r'templates\saludo_template.html') # ruta relativa
    template = Template(archivo_abierto.read())
    archivo_abierto.close()
    
    contexto = Context(datos)
    
    template_renderizaro = template.render(contexto)
    
    return HttpResponse(template_renderizaro)