from django.contrib.auth.models import User

from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer


# esse bloco de imports vai ser utilizado para gerar uma root view
from rest_framework.decorators import api_view

from rest_framework.reverse import reverse # o que é um reverse relationship? é tipo buscar o author de um post...



# para snippet vamos herdar de ModelViewSet e para user vamos herdar de ReadOnlyModelViewSet
class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    # tudo que não for create, update, delete pode ser feito usando esse @action decorator
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# vamos substituir UserList e UserDetail por uma viewset apenas
# normalmente List (list action) e Detail (retrieve action)
# ViewSets vai juntar diferentes views. Lembrar que em django views é mais ou menos o controller.
# Basicamente viewsets diz o que fazer em caso de list, detail, etc
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


# aqui tentamos inserir um root endpoint
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
