from django.contrib import admin
from django.urls import path
from home.views import index, sobre, contato, ajuda


urlpatterns = [
    path('', index, name='index'),  # (aspas vazias = página inicial)
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),  
    path('ajuda/', ajuda, name='ajuda'),
]

