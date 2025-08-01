from django.urls import path
from inicio.views import (
    saludo,
    saludo_template,
    saludo_con_cargador,
    saludo_con_render,
    condicion_y_bucle,
    inicio,
    crear_auto,
    listado_de_autos,
    ver_auto,
    eliminar_auto,
    actualizar_auto
)
# from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    # path('saludo/<str:nombre>/<str:apellido>/', saludo),
    # path('saludo/<str:nombre>/<str:apellido>/', saludo_template),
    # path('saludo/<str:nombre>/<str:apellido>/', saludo_con_cargador),
    path('saludo/<str:nombre>/<str:apellido>/', saludo_con_render, name='saludo'),
    path('template-prueba/', condicion_y_bucle, name='template_prueba'),
    path('autos/', listado_de_autos, name='listado_de_autos'),
    path('autos/crear/', crear_auto, name='crear_auto'),
    path('autos/<int:id_auto>/', ver_auto, name='ver_auto'),
    path('autos/<int:id_auto>/eliminar/', eliminar_auto, name='eliminar_auto'),
    path('autos/<int:id_auto>/actualizar/', actualizar_auto, name='actualizar_auto'),
]
