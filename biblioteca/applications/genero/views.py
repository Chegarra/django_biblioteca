from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Genero


# Inicio para la Ubicación :: inicio
class GeneroInicioTemplateView(TemplateView):
    template_name = 'genero/inicio.html'


# Listar todas la Generos :: listar
class ListAllGeneros(ListView):
    template_name = 'genero/listar_generos.html'
    paginate_by = 12
    ordering = 'nombre'
    context_object_name = 'genero'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        
        lista = Genero.objects.filter(
            nombre__icontains=palabra_clave
        )
        return lista


# Ver la información del genero :: detalles
class GeneroDetailView(DetailView):
    model = Genero
    template_name = 'genero/ver_genero.html'


# Añadir un nuevo genero :: add
class GeneroCreateView(CreateView):
    template_name = "genero/add_genero.html"
    model = Genero
    fields = ('__all__')
    success_url = reverse_lazy('genero_app:listar')

    # def form_valid(self, form):      
    #     return super().form_valid(form)


# Modificar el genero :: edit
class GeneroUpdateView(UpdateView):
    template_name = 'genero/edit_genero.html'
    model = Genero
    fields = ('__all__')
    success_url = reverse_lazy('genero_app:listar')


# Eliminar genero :: delete
class GeneroDeleteView(DeleteView):
    template_name = 'genero/delete_genero.html'
    model = Genero
    fields = ('__all__')
    success_url = reverse_lazy('genero_app:listar')
