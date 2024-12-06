from django.urls import path
from . import views  # Asegúrate de que el archivo views.py exista y tenga las vistas correspondientes

urlpatterns = [
    path('', views.registro, name='registro'),  # Ruta principal para registrar usuarios
    
]

