from django.urls import path
from .views import enviar_mensaje, bandeja_entrada

app_name = 'mensajeria'

urlpatterns = [
    path('enviar_mensaje/', enviar_mensaje, name='enviar_mensaje'),
    path('bandeja_entrada/', bandeja_entrada, name='bandeja_entrada'),
]