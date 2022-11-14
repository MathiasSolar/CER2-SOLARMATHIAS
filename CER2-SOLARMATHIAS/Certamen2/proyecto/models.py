from django.db import models
# Create your models here.

class residencia(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=12)
    def __str__(self):
        return str(self.direccion)
    
class recepcion(models.Model):
    nombre = models.CharField(max_length=30)
    numero = models.PositiveIntegerField()
    fechaentrega = models.DateField()
    estado_eleccion = (('entregado','entregado'), ('no entregado', 'no entregado'))
    estado = models.CharField(max_length=30,choices=estado_eleccion)
    def __str__(self):
        return str(self.numero)
    
