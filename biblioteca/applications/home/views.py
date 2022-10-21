from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView


class InicioView(TemplateView):
    template_name = "home/inicio.html"
