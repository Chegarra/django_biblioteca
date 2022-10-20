from django.urls import path
from . import views


app_name = 'autor_app'

urlpatterns = [
    path(
        'autor/add', 
        views.AutorCreateView.as_view()
        ),
    path(
        'autor/success', 
        views.SuccessView.as_view(), 
        name='correcto'
        ),
    path(
        'autor/edit/<pk>/', 
        views.AutorUpdateView.as_view(), 
        name='editar_autor'
        ),
    path(
        'autor/delete/<pk>/', 
        views.AutorDeleteView.as_view(), 
        name='borrar_autor'
        ),    

]

