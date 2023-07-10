from django.db import models
from datetime import time

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    clave = models.CharField(max_length=255)
    capacidad = models.IntegerField()

    def __str__(self):
        return f"Empresa: {self.nombre} - Capacidad: {self.capacidad}"


class Estacionamiento(models.Model):
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    lugar = models.CharField(max_length=255)
    estado = models.BooleanField(default=False)

    def __str__(self):
        if self.estado:
            return f"Estacionamiento {self.lugar} - Disponible"
        else:
            return f"Estacionamiento {self.lugar} - Ocupado"


class Estado(models.Model):
    id_estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE, related_name='estados')
    hora_ingreso = models.TimeField()
    hora_salida = models.TimeField()

    def __str__(self):
        if self.hora_salida == time(0, 0):
            return f"Hora de Ingreso: {self.hora_ingreso}"
        else:
            return f"Hora de Salida: {self.hora_salida}"
