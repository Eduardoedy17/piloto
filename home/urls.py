from django.contrib import admin
from django.urls import path
from home.views import index, sobre, contato, ajuda
from piloto.home import views


urlpatterns = [
    path('', views.index, name='index'),  # (aspas vazias = página inicial)
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),  
    path('ajuda/', views.ajuda, name='ajuda'),
    path('item/<int:id>/', views.exibir_item, name='exibir_item'),
]

