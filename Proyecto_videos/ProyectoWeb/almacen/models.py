from django.db import models

# Modelo para representar los clientes
class Cliente(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    direccion = models.CharField(max_length=50, verbose_name="Dirección")
    email = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=10, verbose_name="Teléfono")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre


# Modelo para representar las secciones de productos
class SeccionProd(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de la Sección")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "Sección de Producto"
        verbose_name_plural = "Secciones de Productos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


# Modelo para representar los artículos
class Articulos(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre del Artículo")
    seccion = models.ForeignKey(SeccionProd, on_delete=models.CASCADE, verbose_name="Sección")
    imagen = models.ImageField(upload_to="almacen", null=True, blank=True, verbose_name="Imagen")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    disponibilidad = models.BooleanField(default=True, verbose_name="Disponible")
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad en Stock")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"


# Modelo para representar pedidos
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    numero = models.PositiveIntegerField(verbose_name="Número de Pedido")
    fecha = models.DateField(verbose_name="Fecha del Pedido")
    entregado = models.BooleanField(default=False, verbose_name="Entregado")

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-fecha']

    def __str__(self):
        return f"Pedido #{self.numero} de {self.cliente.nombre}"

