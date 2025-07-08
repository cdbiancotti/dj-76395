from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from productos.models import Sarten
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Sartenes(ListView):
    model = Sarten
    template_name = "productos/listado_de_sartenes.html"
    context_object_name = 'sartenes'

class CrearSarten(CreateView):
    model = Sarten
    template_name = "productos/crear_sarten.html"
    fields = ['marca', 'descripcion', 'fecha']
    success_url = reverse_lazy('productos:listado_de_sartenes')
    
class VerSarten(DetailView):
    model = Sarten
    template_name = "productos/ver_sarten.html"

class ActualizarSarten(LoginRequiredMixin, UpdateView):
    model = Sarten
    template_name = "productos/actualizar_sarten.html"
    fields = ['marca', 'descripcion']
    success_url = reverse_lazy('productos:listado_de_sartenes')

class EliminarSarten(LoginRequiredMixin, DeleteView):
    model = Sarten
    template_name = "productos/eliminar_sarten.html"
    success_url = reverse_lazy('productos:listado_de_sartenes')
