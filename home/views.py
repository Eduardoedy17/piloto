from django.shortcuts import render
from django.http import HttpResponse

# Criação da view 'index'
def index(request):
    return render(request, "index.html")

# Criação da view 'sobre'
def sobre(request):
    return render(request, "sobre.html")
# Criação da view 'contato'
def contato(request):
    return render(request, "contato.html")

# Criação da view 'Ajuda'
def ajuda(request): 
    return render(request, "ajuda.html")

# Criação da view 'exibir_item'
def exibir_item(request, id):  
    return render(request, 'exibir_item.html', {'id': id})