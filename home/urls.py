from django.contrib import admin
from django.urls import path
from home.views import index, sobre, contato, ajuda
from home import views


urlpatterns = [
    path('', views.index, name='index'),  # (aspas vazias = página inicial)
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),  
    path('ajuda/', views.ajuda, name='ajuda'),
    path('item/<int:id>/', views.exibir_item, name='exibir_item'),
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
    path('produto/', views.produto, name='produto'),
    path('diasemana/<int:dia_num>/', views.diasemana, name='diasemana'),
]

