from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView


from .models import Autor
from .forms import *

class AutorCreateView(CreateView):
    model = Autor
    template_name = "autor/add_autor.html"
    #  fields = ['nombre', 'apellidos']
    form_class = AutorCreateForm
    success_url = reverse_lazy('autor_app:correcto')

    # def form_valid(self, form):
    #     autor = form.save()
    #     nombre_completo = f'{autor.nombre} {autor.apellidos}'
    #     print(autor)
    #     print(nombre_completo)        
    #     return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'autor/success.html'


class AutorUpdateView(UpdateView):
    template_name = 'autor/edit_autor.html'
    model = Autor
    fields = ('__all__')
    success_url = reverse_lazy('autor_app:correcto')

    # def post(self, requests, *args, **kwargs):
    #     self.object = self.get_object()
    #     print('************** POST **************')
    #     print(requests.POST)
    #     return super().post(requests, *args, *kwargs)

    # def form_valid(self, form):
    #     print('*********** FROM VALID ***********')

    #     return super().form_valid(form)


class AutorDeleteView(DeleteView):
    template_name = 'autor/delete_autor.html'
    model = Autor
    fields = ('__all__')
    success_url = reverse_lazy('autor_app:correcto')