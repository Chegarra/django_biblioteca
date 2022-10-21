from django.urls import path
from . import views

app_name = 'genero_app'

urlpatterns = [
    path(
        'genero/inicio', 
        views.GeneroInicioTemplateView.as_view(), 
        name='inicio'
        ),
    path(
        'genero/lista', 
        views.ListAllGeneros.as_view(), 
        name='listar'
        ),
    path(
        'genero/detalles/<pk>/', 
        views.GeneroDetailView.as_view(),
        name='detalles'
        ),
    path(
        'genero/add',
        views.GeneroCreateView.as_view(), 
        name='add'
        ),
    path(
        'genero/edit/<pk>/', 
        views.GeneroUpdateView.as_view(), 
        name='edit'
        ),
    path(
        'genero/delete/<pk>/', 
        views.GeneroDeleteView.as_view(), 
        name='delete'
        )
]