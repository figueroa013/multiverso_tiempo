from django.shortcuts import render
from .models import EventoNoCanonico
from .Grafo import Grafo

def Control(request):
    # Crear el grafo
    grafo = Grafo()

    # Obtener todos los eventos no canónicos de la base de datos
    eventos = EventoNoCanonico.objects.all()

    # Crear un diccionario para almacenar los nodos
    nodos = []

    # Agregar nodos al grafo
    for evento in eventos:
        
        nodo = {
            'index': evento.id,  # O algún identificador único
            'nombre': evento.nombre,
            'año': evento.año
        }
        grafo.agregar_nodo(evento)
        nodos.append(nodo)

    # Conectar los nodos para formar un ciclo
    num_eventos = len(eventos)
    for i in range(num_eventos):
        grafo.agregar_arista(eventos[i], eventos[(i + 1) % num_eventos])

    # Pasar nodos al contexto
    return render(request, 'Vista_multiverso/pag1.html', {'nodos': nodos})

    
    