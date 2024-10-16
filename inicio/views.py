from django.shortcuts import render, redirect
from inicio.models import Item
from inicio.forms import ItemForm, SearchForm

def home(request):
    items = Item.objects.all()
    search_form = SearchForm()

    if request.method == 'POST' and 'search' in request.POST:
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            items = Item.objects.filter(name__icontains=query)

    return render(request, 'home.html', {'items': items, 'form': ItemForm(), 'search_form': search_form})

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