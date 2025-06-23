<<<<<<< HEAD
from django.db import models

class Asistente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    ci = models.CharField(max_length=20)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=128)  # Considera encriptar la contraseña

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
=======
from django.db import models

# Create your models here.
>>>>>>> d462d4b91c66232b68f2e620e9b127d212d474cf
