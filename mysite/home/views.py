from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Teste Recomendador")

def coletarPreferencias(request):
    # coletas = Coleta.preferencias # retorna todos os objetos
    return render(request,'home/coleta.html')

