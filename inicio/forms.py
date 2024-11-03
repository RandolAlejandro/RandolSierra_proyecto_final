from django import forms
from .models import Item
from django.urls import reverse_lazy

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'anio']
        success_url = reverse_lazy("inicio:home")
    
