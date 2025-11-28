from django.shortcuts import render
from django.http import HttpResponse

# Criação da view 'index'
def index(request):
    return HttpResponse("<h1>Olá, Mundo! Meu site Django está funcionando! 🚀</h1>")