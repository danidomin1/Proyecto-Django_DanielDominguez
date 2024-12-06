from django.shortcuts import render
from .models import Articulos, SeccionProd

def lista_productos(request):
    articulos = Articulos.objects.all()
    return render(request, 'almacen/almacen.html', {'articulos': articulos})
    
def buscar_por_seccion(request):
    # Obtener todas las secciones disponibles
    secciones = SeccionProd.objects.all()
    articulos = None

    # Comprobar si el usuario ha seleccionado una sección
    if 'seccion' in request.GET and request.GET['seccion']:
        seccion_nombre = request.GET['seccion']
        # Filtrar los artículos por el nombre de la sección seleccionada
        articulos = Articulos.objects.filter(seccion__nombre=seccion_nombre)

    # Renderizar la plantilla con las secciones y los artículos filtrados
    return render(request, 'almacen/buscar_por_seccion.html', {
        'secciones': secciones,
        'articulos': articulos
    })

