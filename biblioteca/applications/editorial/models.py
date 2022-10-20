from django.db import models


class Editorial(models.Model):

    nombre = models.CharField('Editorial', max_length=32, unique=True)
    pais = models.CharField('País', max_length=16, blank=True, help_text='País de Origen')
    web = models.URLField('Página Web', max_length=256, blank=True)


    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'
        ordering = ['nombre']


    def __str__(self):
        return f'{self.nombre}'