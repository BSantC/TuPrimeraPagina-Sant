from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from inicio.models import Libro
from inicio.forms import LibroFormulario, BusquedaFormulario
# Create your views here.
def inicio(request):
    
    return render(request, r'inicio\inicio.html')

def cargar_libros(request):
    if request.method== 'POST':  
        formulario=LibroFormulario(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            libro=Libro(titulo=data.get('titulo'), autor=data.get('autor'),abstract=data.get('abstract'))
            libro.save()
        else:
            return render(request, r'inicio\libro_cargado.html', {'formulario':formulario})
    formulario=LibroFormulario()
    return render(request, r'inicio\libro_cargado.html', {'formulario':formulario})

def buscar_libros(request):
    formulario=BusquedaFormulario(request.GET)
    if formulario.is_valid():
        buscar_titulo = formulario.cleaned_data.get('titulo')
        titulos_encontrados = Libro.objects.filter(titulo__icontains=buscar_titulo)  
    else:
        titulos_encontrados = Libro.objects.all()
    formulario=BusquedaFormulario()
    return render(request, r'inicio\libro_buscado.html', {'formulario':formulario, 'titulos_encontrados':titulos_encontrados})
    