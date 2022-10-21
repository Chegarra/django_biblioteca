from django.urls import path
from . import views

app_name = 'autor_app'

urlpatterns = [
    path(
        'autor/inicio', 
        views.AutorInicioTemplateView.as_view(), 
        name='inicio'
        ),
    path(
        'autor/lista',
        views.ListAllAutores.as_view(), 
        name='listar'
        ),
    path(
        'autor/detalles/<pk>/', 
        views.AutorDetailView.as_view(),
        name='detalles'
        ),
    path(
        'autor/add',
        views.AutorCreateView.as_view(), 
        name='add'
        ),
    path(
        'autor/edit/<pk>/', 
        views.AutorUpdateView.as_view(), 
        name='edit'
        ),
    path(
        'autor/delete/<pk>/', 
        views.AutorDeleteView.as_view(), 
        name='delete'
        )
]