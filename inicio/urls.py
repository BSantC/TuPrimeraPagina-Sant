from django.urls import path
from inicio.views import inicio, cargar_libros, buscar_libros 
urlpatterns = [
    path('', inicio, name='inicio'),
    path('libros/cargar/', cargar_libros, name='cargar_libros'),
    path('libros/buscar/',buscar_libros, name='buscar_libros'),
]
