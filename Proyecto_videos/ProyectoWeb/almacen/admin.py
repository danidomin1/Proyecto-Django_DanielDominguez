from django.contrib import admin
from .models import SeccionProd, Articulos

# Modelo admin para SeccionProd
@admin.register(SeccionProd)
class SeccionProdAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("nombre", "created", "updated")
    search_fields = ("nombre",)
    ordering = ("nombre",)


# Modelo admin para Articulos
@admin.register(Articulos)  # Asegúrate de que el nombre sea Articulos
class ArticulosAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("nombre", "seccion", "precio", "disponibilidad", "cantidad", "created", "updated")
    list_filter = ("disponibilidad", "seccion", "created")
    search_fields = ("nombre", "seccion__nombre")
    ordering = ("nombre",)

