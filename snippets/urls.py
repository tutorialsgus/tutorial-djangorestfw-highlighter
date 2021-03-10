from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
	path('users/', views.UserList.as_view()),  # adicionar as views do user
	path('users/<int:pk>/', views.UserDetail.as_view()),
]

# uma maneira de adicionar recursos para extensão .json, .api, .html, etc etc
urlpatterns = format_suffix_patterns(urlpatterns)

# eu tinha duvida se adicionava antes ou deopis do format_suffix, mas realmente aqui parece melhor
	# pra falar a verdade acho que tanto faz botar essa linha no final ou antes do format_suffix
# depois e adicionado vai aparecer um login no canto superior da tela
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]