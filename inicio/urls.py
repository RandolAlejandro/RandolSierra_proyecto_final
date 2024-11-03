from django.urls import path
from inicio.views import home, add_item, about, VerItem, EditarItem, EliminarItem

app_name = "inicio"

urlpatterns = [
    path('', home, name='home'),
    path('agregar/', add_item, name='add_item'),
    path('sobre_mi/', about, name='about'),
    path('item/<int:pk>/ver_mas/', VerItem.as_view(), name='ver_mas'),
    path('item/<int:pk>/editar/', EditarItem.as_view(), name='editar'),
    path('item/<int:pk>/eliminar/', EliminarItem.as_view(), name='eliminar'),
]
