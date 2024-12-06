from django.urls import path
from . import views

urlpatterns = [
    path('', views.soporte_view, name='soporte'),  # Página principal de soporte
    path('descargar-anydesk/', views.descargar_anydesk, name='descargar_anydesk'),  # Redirige a AnyDesk
    path('ir-a-sharp/', views.ir_a_sharp, name='ir_a_sharp'),  # Redirige al centro de Sharp
]

