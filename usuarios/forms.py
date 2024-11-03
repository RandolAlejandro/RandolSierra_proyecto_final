from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserChangeForm

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class FormularioEdicionPerfil(UserChangeForm):
    username = forms.CharField()
    email = forms.EmailField()
    password = None
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'avatar']