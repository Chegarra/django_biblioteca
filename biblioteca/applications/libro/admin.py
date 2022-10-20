from django.contrib import admin
from .models import *

from applications.autor.models import Autor

class LibroAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'genero',
        'editorial',
        'isbn',
        'ubicacion',
        'id'

    )

    search_fields = ('titulo', 'isbn')
    list_filter = ('autor', 'genero', 'editorial', 'ubicacion')


admin.site.register(Libro, LibroAdmin)