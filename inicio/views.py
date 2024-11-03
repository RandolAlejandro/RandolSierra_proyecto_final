from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Item
from inicio.forms import ItemForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio:home')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

def about(request):
    return render(request, 'about.html')

class VerItem(LoginRequiredMixin, DetailView):
    Model = Item
    template_name = "ver_mas.html"
    context_object_name = 'item'
    
    def get_queryset(self):
        return Item.objects.all()

class EditarItem(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = "editar.html"
    success_url = reverse_lazy('inicio:home')
    fields = ['name', 'anio']

class EliminarItem(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = "eliminar.html"
    success_url = reverse_lazy('inicio:home')
