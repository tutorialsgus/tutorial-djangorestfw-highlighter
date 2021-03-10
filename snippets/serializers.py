from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

from django.contrib.auth.models import User

# ModelSerializer tem muito menos linhas de código do que um Serializer
# Simple default implementations for the create() and update() methods.
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') # readonly é bom para read-only, mas não é bom para updating
    class Meta:
        model = Snippet
        fields = ['id', 'owner', 'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    # snippets é um reverse relationship on the User model, por isso adicionamos na mão

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']