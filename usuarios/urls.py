from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView
from .views import Register, CambiarPassword

app_name = "usuarios"

urlpatterns = [
    path('registrate/', Register.as_view(), name='registro'),
    path('perfil/editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('perfil/editar_contraseña/', CambiarPassword.as_view(), name='editar_contraseña'),
    path('iniciar_sesion/', views.login_view, name='login'),
    path('cerrar_sesion/', LogoutView.as_view(), name='logout')
]