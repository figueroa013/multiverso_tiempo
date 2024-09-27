from django.shortcuts import render
from .models import EventoNoCanonico
from .Grafo import Grafo
import json

def Control2(request):
    # Crear el grafo
    grafo = Grafo()

    # Obtener todos los eventos no canónicos de la base de datos
    eventos = EventoNoCanonico.objects.all()

    # Crear listas para almacenar los nodos y aristas
    nodos = []
    aristas = []

    # Agregar nodos al grafo
    for evento in eventos:
        nodo = {
            'id': evento.id,
            'label': evento.nombre,
            'title': f"Año: {evento.año}"
        }
        grafo.agregar_nodo(evento)
        nodos.append(nodo)

    # Conectar los nodos para formar un ciclo
    num_eventos = len(eventos)
    for i in range(num_eventos):
        source = eventos[i].id
        target = eventos[(i + 1) % num_eventos].id
        grafo.agregar_arista(eventos[i], eventos[(i + 1) % num_eventos])
        arista = {'from': source, 'to': target}
        aristas.append(arista)

    # Serializar nodos y aristas a JSON
    nodos_json = json.dumps(nodos)
    aristas_json = json.dumps(aristas)

    # Pasar nodos y aristas al contexto
    context = {
        'nodos': nodos_json,
        'aristas': aristas_json
    }

    return render(request, 'Vista_multiverso/pag_grafo.html', context)
