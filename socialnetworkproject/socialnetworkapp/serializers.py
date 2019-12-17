from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('user', 'created', 'group', 'last_updated', 'text')
        model = Post