from django.db import models

class Autor(models.Model):

    nombre = models.CharField('Nombre', max_length=32)
    apellidos = models.CharField('Apellidos', max_length=32)
    # foto = models.ImageField(upload_to='autor', blank=True, null=True)
    # nombre_completo = models.CharField('Nombre completo', max_length=64, blank=True)


    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['apellidos', 'nombre']


    def __str__(self):
        return f'{self.apellidos}, {self.nombre}'