from django.contrib import admin
from django.urls import include, path
from home.views import index, sobre, contato, ajuda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),    
]