from django.shortcuts import render
from django.http import HttpResponse

# View 'index'
def index(request):
    return render(request, "index.html")

# View 'sobre'
def sobre(request):
    return render(request, "sobre.html")
# View 'contato'
def contato(request):
    return render(request, "contato.html")

# View 'Ajuda'
def ajuda(request): 
    return render(request, "ajuda.html")

# View 'exibir_item'
def exibir_item(request, id):  
    return render(request, 'exibir_item.html', {'id': id})

# View 'perfil'
def perfil(request, usuario):  
    return render(request, 'perfil.html', {'usuario': usuario})

def produto(request):
    return render(request, 'produto.html')

# View 'dia_semana'
def diasemana(request, dia_num):
    # Dicionário com os dias
    dias = {
        1: 'Domingo',
        2: 'Segunda-feira',
        3: 'Terça-feira',
        4: 'Quarta-feira',
        5: 'Quinta-feira',
        6: 'Sexta-feira',
        7: 'Sábado'
    }
    
    # Busca o dia, se não achar retorna 'Dia inválido'
    resultado = dias.get(dia_num, 'Dia inválido')
    
    return render(request, 'diasemana.html', {'dia': resultado})