from django.urls import path
from inicio.views import saludo, saludo_template, saludo_con_cargador, saludo_con_render, condicion_y_bucle, inicio, crear_auto

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    # path('saludo/<str:nombre>/<str:apellido>/', saludo),
    # path('saludo/<str:nombre>/<str:apellido>/', saludo_template),
    # path('saludo/<str:nombre>/<str:apellido>/', saludo_con_cargador),
    path('saludo/<str:nombre>/<str:apellido>/', saludo_con_render, name='saludo'),
    path('template-prueba/', condicion_y_bucle, name='template_prueba'),
    path('auto/crear/', crear_auto, name='crear_auto')
]
