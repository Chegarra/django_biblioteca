from django.urls import path
from . import views

app_name = 'libro_app'

urlpatterns = [
    path(
        'libro/inicio', 
        views.LibroInicioTemplateView.as_view(), 
        name='inicio'
        ),
    path(
        'libro/lista', 
        views.ListAllLibros.as_view(), 
        name='listar'
        ),
    path(
        'libro/detalles/<pk>/', 
        views.LibroDetailView.as_view(),
        name='detalles'
        ),
    path(
        'libro/add',
        views.LibroCreateView.as_view(), 
        name='add'
        ),
    path(
        'libro/edit/<pk>/', 
        views.LibroUpdateView.as_view(), 
        name='edit'
        ),
    path(
        'libro/delete/<pk>/', 
        views.LibroDeleteView.as_view(), 
        name='delete'
        )
]