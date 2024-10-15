from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}, {self.edad} años'
