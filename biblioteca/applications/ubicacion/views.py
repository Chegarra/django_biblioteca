from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView


from .models import Ubicacion
from .forms import *

class UbicacionCreateView(FormView):

    model = Ubicacion
    template_name = "ubicacion/add_ubicacion.html"
    form_class = AddUbicacionForm
    success_url = reverse_lazy('ubicacion_app:correcto')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        codigo = form.cleaned_data['codigo']
        descripcion = form.cleaned_data['descripcion']

        Ubicacion.objects.create(
            nombre=nombre,
            codigo=codigo,
            descripcion=descripcion
        )

        print('*********** FORM VALID ***********')   
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'autor/success.html'