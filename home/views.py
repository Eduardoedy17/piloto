from django.shortcuts import render
from django.http import HttpResponse

# Criação da view 'index'
def index(request):
    return HttpResponse("<h1>Pagina Principal - Teste 🚀</h1>")

# Criação da view 'sobre'
def sobre(request):
    return HttpResponse("<h1>Sobre o Sistema Django! - Teste 🚀</h1>")

# Criação da view 'contato'
def contato(request):
    return HttpResponse("<h1>Contato - Teste 🚀</h1>")

# Criação da view 'Ajuda'
def ajuda(request): 
    return HttpResponse("<h1>Ajuda - Teste 🚀</h1>")