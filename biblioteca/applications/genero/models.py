from django.db import models


class Genero(models.Model):
    nombre = models.CharField('Género', max_length=32, unique=True)
    codigo = models.CharField('Código', max_length=16, unique=True, help_text='XXXX-YYYY')


    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
        ordering = ['nombre', 'codigo']


    def __str__(self):
        return f'{self.nombre} - ({self.codigo})'