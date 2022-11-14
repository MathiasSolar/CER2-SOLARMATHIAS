from django.shortcuts import render, HttpResponse
from .models import recepcion

# Create your views here.

def inicio (request):
    recepciones = recepcion.objects.all()
    busqueda = request.GET.get('buscar')
    if busqueda != "" and busqueda is not None:
        recepciones = recepciones.filter(numero=busqueda)
    return render(request, "proyecto/inicio.html", {"recepciones":recepciones})