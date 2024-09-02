from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name="INICIO"),
    path('multiverso/', views.multi, name="multiverso"),
    
]
