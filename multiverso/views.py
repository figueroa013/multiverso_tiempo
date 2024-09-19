from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .Control import Control
from .models import EventoNoCanonico
# Create your views here.
def index(request):
    return render(request, 'Vista_multiverso/index.html', )  

def multi(request):
    return Control(request)

def imprimir_indice(request):
    current_index = request.POST.get('current_index')
    print(f"Índice actual: {current_index}")
    return HttpResponse(f"Índice {current_index} impreso en la consola del servidor")


def pag2(request, id):
    evento = get_object_or_404(EventoNoCanonico, id=id)
    return render(request, 'Vista_multiverso/pag2.html', {'evento': evento})