from django.db import models



class Usuario(models.Model):
    nombre_cuenta = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    correo_electronico = models.EmailField(max_length=254, unique=True, default='example@example.com')
    contraseña = models.CharField(max_length=128)


    def __str__(self):
        return self.username

