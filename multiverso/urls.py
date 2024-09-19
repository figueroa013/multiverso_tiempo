from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="INICIO"),
    path('multiverso/', views.multi, name="multiverso"),
    path('pag2/<int:id>/', views.pag2, name='pag2'),  # Recibe el índice del nodo
    path('imprimir-indice/', views.imprimir_indice, name='imprimir_indice'),
]
