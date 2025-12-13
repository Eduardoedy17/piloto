from django.shortcuts import render, redirect # Importar redirect
from .forms import ContatoForm, ProdutoForm

# --- BANCO DE DADOS EM MEMÓRIA (GLOBAL) ---
# Definimos a lista fora das funções para que todas as views acessem a mesma lista
lista_produtos = [
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
]

# --- VIEWS ---

def index(request):
    context = {
        "data": "05/12/2025",
        "cidade": "Teresina",
        "ip": "127.0.0.1",
    }
    return render(request, "index.html", context)

def sobre(request):
    return render(request, "sobre.html")

def contato(request):
    form = ContatoForm()
    context = {'form': form}
    return render(request, 'contato.html', context)

def ajuda(request): 
    return render(request, "ajuda.html")

def perfil(request, usuario):  
    return render(request, 'perfil.html', {'usuario': usuario})

def exibir_item(request, id):  
    return render(request, 'exibir_item.html', {'id': id})

def diasemana(request, dia_num):
    dias = {
        1: 'Domingo', 2: 'Segunda-feira', 3: 'Terça-feira',
        4: 'Quarta-feira', 5: 'Quinta-feira', 6: 'Sexta-feira', 7: 'Sábado'
    }
    resultado = dias.get(dia_num, 'Dia inválido')
    return render(request, 'diasemana.html', {'dia': resultado})

# --- VIEWS DE PRODUTO ---

def produto(request):
    # Agora usamos a lista global
    context = {'lista': lista_produtos}
    return render(request, 'produto/lista.html', context)

def produtoform(request):
    # Formulário vazio para cadastro
    form = ProdutoForm()
    return render(request, 'produto/formulario.html', {'form': form})

def detalhes_produto(request, id):
    produto_encontrado = None
    # Procura o produto na lista pelo ID
    for item in lista_produtos:
        if item['id'] == id:
            produto_encontrado = item
            break

    contexto = {
        'produto': produto_encontrado,
        'id': id # Mantemos o ID caso o produto não seja encontrado
    }
    return render(request, 'produto/detalhes.html', contexto)

def editar_produto(request, id):
    # 1. Procurar o produto na lista pelo ID
    produto_encontrado = None
    for item in lista_produtos:
        if item['id'] == id:
            produto_encontrado = item
            break
    
    # 2. Se achou, preenche o formulário (initial)
    if produto_encontrado:
        # Preenche os campos com os dados existentes
        # Nota: O preço está como string '2.500,00', o form pode reclamar se for DecimalField,
        # mas para exibir na tela funciona.
        form = ProdutoForm(initial={
            'nome': produto_encontrado['nome'],
            'preco': produto_encontrado['preco'] 
        })
    else:
        # Se não achar (erro), abre vazio
        form = ProdutoForm()

    contexto = {
        'form': form,
        'id': id
    }
    return render(request, 'produto/formulario.html', contexto)

def excluir_produto(request, id):
    # Se o método for POST, significa que o usuário clicou em "Confirmar Exclusão"
    if request.method == "POST":
        for item in lista_produtos:
            if item['id'] == id:
                lista_produtos.remove(item) # Remove da lista
                break
        return redirect('produto') # Redireciona de volta para a lista

    # Se for GET, apenas mostra a página de confirmação
    return render(request, 'produto/excluir.html', {'id': id})