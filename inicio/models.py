from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    dni = models.IntegerField()
    edad = models.IntegerField()

    def __str__(self):
        return f'Nombre: {self.nombre.capitalize()}. Apellido: {self.apellido.capitalize()}. D.N.I: {self.dni}'