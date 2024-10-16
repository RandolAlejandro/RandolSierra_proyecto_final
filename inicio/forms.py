from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

class SearchForm(forms.Form):
    query = forms.CharField(label='', max_length=100)