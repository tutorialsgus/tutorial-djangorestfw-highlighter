from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list), # cuida das views para listar snippets
    path('snippets/<int:pk>/', views.snippet_detail),  # lista detalhes de uma snippet em específico
]