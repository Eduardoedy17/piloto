from django.contrib import admin
from django.urls import path
from home.views import index  # <--- Adicione esta importação

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # <--- Adicione esta linha (aspas vazias = página inicial)
]