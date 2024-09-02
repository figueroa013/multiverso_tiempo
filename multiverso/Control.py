from django.shortcuts import render
from .Nodo import Nodo
from .Grafo import Grafo
from .EventoNoCanonico import EventoNoCanonico

def Control(request):
    # Crear instancias de EventoNoCanonico
    evento1 = EventoNoCanonico(2020, "Evento A", "Descripción del caso 1", "Descripción del caso 2")
    evento2 = EventoNoCanonico(2021, "Evento B", "Descripción del caso 3", "Descripción del caso 4")
    evento3 = EventoNoCanonico(2022, "Evento C", "Descripción del caso 5", "Descripción del caso 6")
    
    # Crear el grafo
    grafo = Grafo()

    # Agregar nodos al grafo
    grafo.agregar_nodo(evento1)
    grafo.agregar_nodo(evento2)
    grafo.agregar_nodo(evento3)

    # Conectar los nodos (crear aristas)
    grafo.agregar_arista(evento1, evento2)
    grafo.agregar_arista(evento2, evento3)
    grafo.agregar_arista(evento3, evento1)  # Esto crea un ciclo

    # Pasar nodos como texto al contexto
    nodos = [
        {evento1.nombre},
        {evento2.nombre},
        {evento3.nombre}
    ]

    return render(request, 'Vista_multiverso/pag1.html', {'nodos': nodos})
     
   