from django.urls import path
from . import views

app_name = 'editorial_app'

urlpatterns = [
    path(
        'editorial/inicio', 
        views.EditorialInicioTemplateView.as_view(), 
        name='inicio'
        ),
    path(
        'editorial/lista', 
        views.ListAllEditoriales.as_view(), 
        name='listar'
        ),
    path(
        'editorial/detalles/<pk>/', 
        views.EditorialDetailView.as_view(),
        name='detalles'
        ),
    path(
        'editorial/add',
        views.EditorialCreateView.as_view(), 
        name='add'
        ),
    path(
        'editorial/edit/<pk>/', 
        views.EditorialUpdateView.as_view(), 
        name='edit'
        ),
    path(
        'editorial/delete/<pk>/', 
        views.EditorialDeleteView.as_view(), 
        name='delete'
        )
]