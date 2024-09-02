from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .Control import Control

# Create your views here.
def index(request):
    return render(request, 'index.html', )  

def multi(request):
    return Control(request)


