from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Ubicacion


# Inicio para la Ubicación :: inicio
class UbicacionInicioTemplateView(TemplateView):
    template_name = 'ubicacion/inicio.html'


# Listar todas la Ubicaciones :: listar
class ListAllUbicaciones(ListView):
    template_name = 'ubicacion/listar_ubicaciones.html'
    paginate_by = 12
    ordering = 'nombre'
    context_object_name = 'ubicacion'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        
        lista = Ubicacion.objects.filter(
            nombre__icontains=palabra_clave
        )
        return lista


# Ver la información del ubicacion :: detalles
class UbicacionDetailView(DetailView):
    model = Ubicacion
    template_name = 'ubicacion/ver_ubicacion.html'


# Añadir un nuevo ubicacion :: add
class UbicacionCreateView(CreateView):
    template_name = "ubicacion/add_ubicacion.html"
    model = Ubicacion
    fields = ('__all__')
    success_url = reverse_lazy('ubicacion_app:listar')

    # def form_valid(self, form):      
    #     return super().form_valid(form)


# Modificar el ubicacion :: edit
class UbicacionUpdateView(UpdateView):
    template_name = 'ubicacion/edit_ubicacion.html'
    model = Ubicacion
    fields = ('__all__')
    success_url = reverse_lazy('ubicacion_app:listar')


# Eliminar ubicacion :: delete
class UbicacionDeleteView(DeleteView):
    template_name = 'ubicacion/delete_ubicacion.html'
    model = Ubicacion
    fields = ('__all__')
    success_url = reverse_lazy('ubicacion_app:listar')
