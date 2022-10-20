from django.urls import path
from . import views

urlpatterns = [
    path('libro/listar_libros', views.ListAllLibros.as_view()),
    path('libro/listar_libros_por_autor/<autor>/', views.ListAllLibrosByAutor.as_view()),
    path('libro/listar_libros_por_kwords', views.ListLibrosByKwords.as_view()),
    path('libro/ver_libro/<pk>/', views.LibroDetailView.as_view())


]