from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    año = models.IntegerField()
    
    def __str__(self):
        return f'{self.modelo} {self.año}'