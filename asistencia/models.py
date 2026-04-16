from django.db import models

class Asistencia(models.Model):
    nombre_completo = models.CharField(max_length=150)
    documento_de_identidad = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    fecha_de_asistencia = models.DateField()
    hora_de_ingreso = models.TimeField()
    hora_de_salida = models.TimeField()
    presente = models.BooleanField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_completo