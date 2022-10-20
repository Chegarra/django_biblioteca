from typing import List
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Libro


class ListAllLibros(ListView):
    template_name = 'libro/listar_libros.html'
    model = Libro
    paginate_by = 1
    ordering = 'titulo'
    # context_object_name = 'libros'

    # def get_queryset(self):

    #     lista = Libro.objects.filter(
    #         autor__nombre='Arturo'
    #     )
    #     return lista


class ListAllLibrosByAutor(ListView):
    template_name = 'libro/listar_libros_by_autor.html'
    # model = Libro
    # context_object_name = 'libros'

    def get_queryset(self):

        busqueda = self.kwargs['autor']
        print(busqueda)

        libro = Libro.objects.get(id=4)
        print(libro.autor.all())

        lista = Libro.objects.filter(
            autor__nombre=busqueda
        )

        print(lista)
        return lista


class ListLibrosByKwords(ListView):

    template_name = 'libro/listar_libros_by_kwords.html'
    context_object_name = 'libros'

    def get_queryset(self):
        kword = self.request.GET.get('kwords', '')

        lista = Libro.objects.filter(
            editorial__nombre=kword
        )

        return lista

class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libro/ver_libro.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['estrella'] = 'El mejor libro'

        return context
