from django.db import models

from applications.autor.models import Autor
from applications.editorial.models import Editorial
from applications.genero.models import Genero
from applications.ubicacion.models import Ubicacion


class Libro(models.Model):

    titulo = models.CharField(
        'Título', 
        max_length=64
        )

    autor = models.ManyToManyField(
        Autor
        )

    genero = models.ForeignKey(
        Genero,
        on_delete=models.CASCADE
        )

    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.CASCADE
        )

    isbn = models.CharField(
        'ISBN', 
        max_length=16, 
        unique=True
        )

    # foto = models.ImageField(
    #     upload_to='libros',
    #     blank=True,
    #     null=True
    #     )

    ubicacion = models.ForeignKey(
        Ubicacion,
        on_delete=models.CASCADE
        )

    resumen = models.CharField(
        'Resumen', 
        max_length=1024, 
        blank=True
        )

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']


    def __str__(self):
        return f'{self.titulo}'