from django.urls import path
from inicio.views import saludo, saludo_template, saludo_con_cargador, saludo_con_render, condicion_y_bucle, inicio, crear_auto

urlpatterns = [
    path('', inicio),
    # path('saludo/<str:nombre>/<str:apellido>/', saludo),
    # path('saludo/<str:nombre>/<str:apellido>/', saludo_template),
    # path('saludo/<str:nombre>/<str:apellido>/', saludo_con_cargador),
    path('saludo/<str:nombre>/<str:apellido>/', saludo_con_render),
    path('template-prueba/', condicion_y_bucle),
    path('auto/crear/<str:marca>/<str:modelo>/', crear_auto)
]
