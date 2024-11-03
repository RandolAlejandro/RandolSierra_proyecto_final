from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Mensaje(models.Model):
    remitente = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mensajes_enviados', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f'Mensaje de {self.remitente} a {self.destinatario}'