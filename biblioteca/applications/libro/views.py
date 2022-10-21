from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Libro


# Inicio para los Libros :: inicio
class LibroInicioTemplateView(TemplateView):
    template_name = 'libro/inicio.html'


# Listar todos los libros :: listar
class ListAllLibros(ListView):
    template_name = 'libro/listar_libros.html'
    # model = Libro
    paginate_by = 12
    ordering = 'titulo'
    context_object_name = 'libros'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        
        lista = Libro.objects.filter(
            titulo__icontains=palabra_clave
        )
        return lista


# Ver la información del libro :: detalles
class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libro/ver_libro.html'


# Añadir un nuevo libro :: add
class LibroCreateView(CreateView):
    template_name = "libro/add_libro.html"
    model = Libro
    fields = ('__all__')
    success_url = reverse_lazy('libro_app:listar')

    # def form_valid(self, form):      
    #     return super().form_valid(form)


# Modificar el libro :: edit
class LibroUpdateView(UpdateView):
    template_name = 'libro/edit_libro.html'
    model = Libro
    fields = ('__all__')
    success_url = reverse_lazy('libro_app:listar')


# Eliminar libro :: delete
class LibroDeleteView(DeleteView):
    template_name = 'libro/delete_libro.html'
    model = Libro
    fields = ('__all__')
    success_url = reverse_lazy('libro_app:listar')
