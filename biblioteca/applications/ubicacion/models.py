from django.db import models

class Ubicacion(models.Model):

    nombre = models.CharField('Ubicación', max_length=32, unique=True )
    codigo = models.CharField('Código', max_length=16, unique=True, help_text='XXXX-YYYY')
    descripcion = models.CharField('Descripción', max_length=256, blank=True, help_text='¿Donde está ubicado?')


    class Meta:
        verbose_name = 'Ubicación'
        verbose_name_plural = 'Ubicaciones'
        ordering = ['nombre', 'codigo']


    def __str__(self):
        return f'{self.nombre} ({self.codigo})'
