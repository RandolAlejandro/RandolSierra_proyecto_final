from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroUsuarioForm, FormularioEdicionPerfil
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def login_view(request):

    formulario = AuthenticationForm()

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario_name = formulario.cleaned_data.get("username")
            contraseña = formulario.cleaned_data.get("password")

            usuario = authenticate(username=usuario_name, password=contraseña)

            login(request, usuario)

            return redirect("inicio:home")

    return render(request, "usuarios/login.html", {"form": formulario})

class Register(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'usuarios/register.html'
    success_url = reverse_lazy('usuarios:login')
    
def editar_perfil(request):
    formulario = FormularioEdicionPerfil(instance=request.user)
    
    if request.method == "POST":
        formulario = FormularioEdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect("inicio:home")
         
    return render(request, "usuarios/editar_perfil.html", {"form": formulario})

class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/editar_contraseña.html'
    success_url = reverse_lazy('usuarios:editar_perfil')