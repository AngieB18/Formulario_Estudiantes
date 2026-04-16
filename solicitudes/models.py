from django.db import models

TIPOS = [
    ('academica', 'Académica'),
    ('administrativa', 'Administrativa'),
    ('tecnica', 'Técnica'),
    ('otra', 'Otra'),
]

class Solicitud(models.Model):
    nombre_solicitante = models.CharField(max_length=150)
    documento_identidad = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    telefono_contacto = models.IntegerField()
    tipo_solicitud = models.CharField(max_length=20, choices=TIPOS)
    asunto = models.CharField(max_length=200)
    descripcion_detallada = models.TextField()
    fecha_solicitud = models.DateField()
    archivo_adjunto = models.FileField(upload_to='adjuntos/', blank=True, null=True)