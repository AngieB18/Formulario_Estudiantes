from django.db import models

class Solicitud(models.Model):
    TIPO_SOLICITUD = [
        ('academica', 'Académica'),
        ('administrativa', 'Administrativa'),
        ('tecnica', 'Técnica'),
        ('otra', 'Otra'),
    ]

    nombre = models.CharField("Nombre del solicitante", max_length=150)
    documento = models.CharField("Documento de identidad", max_length=50)
    correo = models.EmailField("Correo electrónico")
    telefono = models.CharField("Teléfono de contacto", max_length=20)
    tipo = models.CharField("Tipo de solicitud", max_length=20, choices=TIPO_SOLICITUD)
    asunto = models.CharField("Asunto", max_length=200)
    descripcion = models.TextField("Descripción detallada")
    fecha = models.DateField("Fecha de la solicitud")
    archivo = models.FileField("Archivo adjunto", upload_to='archivos/', null=True, blank=True)

    def __str__(self):
        return self.nombre