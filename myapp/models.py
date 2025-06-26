from django.db import models

class Asistente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    ci = models.CharField(max_length=20)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=128)  # Considera encriptar la contraseña
    puntos_asistencia = models.IntegerField(default=0)
    puntos_comida = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"