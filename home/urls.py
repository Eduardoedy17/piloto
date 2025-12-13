from django.urls import path
from home import views

urlpatterns = [
    # Rotas originais
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),  
    path('ajuda/', views.ajuda, name='ajuda'),
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
    path('item/<int:id>/', views.exibir_item, name='exibir_item'),
    path('diasemana/<int:dia_num>/', views.diasemana, name='diasemana'),
    
    # Rota principal de produtos
    path('produto/', views.produto, name='produto'),
    
    # --- O QUE FALTA ADICIONAR: ---
    
    # Rota para o formulário (necessária para o botão "Adicionar Produto")
    path('produto/form/', views.produtoform, name='produtoform'),

    # Rotas para os botões de ação (Exercício)
    path('produtos/detalhes/<int:id>/', views.detalhes_produto, name='detalhes_produto'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('produtos/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),
]