from django.urls import path
from . import views

app_name = 'ubicacion_app'

urlpatterns = [
    path(
        'ubicacion/inicio', 
        views.UbicacionInicioTemplateView.as_view(), 
        name='inicio'
        ),
    path(
        'ubicacion/lista', 
        views.ListAllUbicaciones.as_view(), 
        name='listar'
        ),
    path(
        'ubicacion/detalles/<pk>/', 
        views.UbicacionDetailView.as_view(),
        name='detalles'
        ),
    path(
        'ubicacion/add',
        views.UbicacionCreateView.as_view(), 
        name='add'
        ),
    path(
        'ubicacion/edit/<pk>/', 
        views.UbicacionUpdateView.as_view(), 
        name='edit'
        ),
    path(
        'ubicacion/delete/<pk>/', 
        views.UbicacionDeleteView.as_view(), 
        name='delete'
        )
]