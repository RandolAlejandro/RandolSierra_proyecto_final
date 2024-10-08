from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse("Hola soy la vista")