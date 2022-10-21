from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Editorial


# Inicio para la Ubicación :: inicio
class EditorialInicioTemplateView(TemplateView):
    template_name = 'editorial/inicio.html'


# Listar todas la Editoriales :: listar
class ListAllEditoriales(ListView):
    template_name = 'editorial/listar_editoriales.html'
    paginate_by = 12
    ordering = 'nombre'
    context_object_name = 'editorial'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        
        lista = Editorial.objects.filter(
            nombre__icontains=palabra_clave
        )
        return lista


# Ver la información del editorial :: detalles
class EditorialDetailView(DetailView):
    model = Editorial
    template_name = 'editorial/ver_editorial.html'


# Añadir un nueva editorial :: add
class EditorialCreateView(CreateView):
    template_name = "editorial/add_editorial.html"
    model = Editorial
    fields = ('__all__')
    success_url = reverse_lazy('editorial_app:listar')

    # def form_valid(self, form):      
    #     return super().form_valid(form)


# Modificar el editorial :: edit
class EditorialUpdateView(UpdateView):
    template_name = 'editorial/edit_editorial.html'
    model = Editorial
    fields = ('__all__')
    success_url = reverse_lazy('editorial_app:listar')


# Eliminar editorial :: delete
class EditorialDeleteView(DeleteView):
    template_name = 'editorial/delete_editorial.html'
    model = Editorial
    fields = ('__all__')
    success_url = reverse_lazy('editorial_app:listar')
