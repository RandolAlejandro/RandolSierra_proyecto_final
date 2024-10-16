from django.urls import path
from inicio.views import home, add_item, about

app_name = "inicio"

urlpatterns = [
    path('', home, name='home'),
    path('agregar/', add_item, name='add_item'),
    path('sobre_mi/', about, name='about'),
]
