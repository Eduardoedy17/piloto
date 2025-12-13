from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContatoForm, ProdutoForm

# View 'index'
def index(request):
    context = {
        "data": "05/12/2025",
        "cidade": "Teresina",
        "ip": "127.0.0.1",
    }
    return render(request, "index.html", context)

# View 'sobre'
def sobre(request):
    return render(request, "sobre.html")
#view contato
def contato(request):
    form = ContatoForm()
    context = {
        'form': form,
    }
    return render(request, 'contato.html', context)

# View 'Ajuda'
def ajuda(request): 
    return render(request, "ajuda.html")

# View 'perfil': Pega o texto da URL e manda para a tela
def perfil(request, usuario):  
    return render(request, 'perfil.html', {'usuario': usuario})

# View 'exibir_item': Pega o ID da URL e manda para a tela
def exibir_item(request, id):  
    return render(request, 'exibir_item.html', {'id': id})

# View 'produto'
def produto(request):
    context = {
        'lista': [
            {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
            {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
            {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
            {'id': 4, 'nome': 'Mouse', 'preco': '40,00'},
            {'id': 5, 'nome': 'Impressora', 'preco': '600,00'},
            {'id': 6, 'nome': 'Scanner', 'preco': '700,00'},
            {'id': 7, 'nome': 'Câmera Web', 'preco': '150,00'},
            {'id': 8, 'nome': 'Headset', 'preco': '120,00'},
            {'id': 9, 'nome': 'Pendrive 32GB', 'preco': '30,00'},
            {'id': 10, 'nome': 'HD Externo 1TB', 'preco': '350,00'},
            {'id': 11, 'nome': 'Estabilizador', 'preco': '200,00'},
            {'id': 12, 'nome': 'Switch 8 portas', 'preco': '180,00'},
            {'id': 13, 'nome': 'Roteador Wi-Fi', 'preco': '220,00'},
        ],
    }
    return render(request, 'produto/lista.html', context)


def produtoform(request):
    form = ProdutoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'produto/form.html', contexto)


# View 'dia da semana'
def diasemana(request, dia_num):
    # Dicionário com os dias da semana
    dias = {
        1: 'Domingo',
        2: 'Segunda-feira',
        3: 'Terça-feira',
        4: 'Quarta-feira',
        5: 'Quinta-feira',
        6: 'Sexta-feira',
        7: 'Sábado'
    }
    # Obtém o dia correspondente ou uma mensagem de erro
    resultado = dias.get(dia_num, 'Dia inválido')
    return render(request, 'diasemana.html', {'dia': resultado})