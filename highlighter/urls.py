from django.contrib import admin
from django.urls import path, include # adicionar o include pra botar urls de outros apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')), # atualiza para adicionar coisas do app snippets
]
