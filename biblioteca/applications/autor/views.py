from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Autor


# Inicio para la Ubicación :: inicio
class AutorInicioTemplateView(TemplateView):
    template_name = 'autor/inicio.html'


# Listar todos los Autores :: listar
class ListAllAutores(ListView):
    template_name = 'autor/listar_autores.html'
    paginate_by = 12
    ordering = 'nombre'
    context_object_name = 'autor'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        
        lista = Autor.objects.filter(
            nombre__icontains=palabra_clave
        )
        return lista


# Ver la información del autor :: detalles
class AutorDetailView(DetailView):
    model = Autor
    template_name = 'autor/ver_autor.html'


# Añadir un nuevo autor :: add
class AutorCreateView(CreateView):
    template_name = "autor/add_autor.html"
    model = Autor
    fields = ('__all__')
    success_url = reverse_lazy('autor_app:listar')

    # def form_valid(self, form):      
    #     return super().form_valid(form)


# Modificar el autor :: edit
class AutorUpdateView(UpdateView):
    template_name = 'autor/edit_autor.html'
    model = Autor
    fields = ('__all__')
    success_url = reverse_lazy('autor_app:listar')


# Eliminar autor :: delete
class AutorDeleteView(DeleteView):
    template_name = 'autor/delete_autor.html'
    model = Autor
    fields = ('__all__')
    success_url = reverse_lazy('autor_app:listar')
