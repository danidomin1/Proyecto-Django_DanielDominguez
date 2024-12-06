from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='Almacen'),
    path('buscar-por-seccion/', views.buscar_por_seccion, name='buscar_por_seccion'),
]

