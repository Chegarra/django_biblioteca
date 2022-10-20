from django.urls import path
from . import views


app_name = 'ubicacion_app'

urlpatterns = [
    path(
        'ubicacion/add', 
        views.UbicacionCreateView.as_view(),
        name='add'
        ),
    path(
        'ubicacion/success', 
        views.SuccessView.as_view(), 
        name='correcto'
        )
]

