from rest_framework import serializers

from .models import Author

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'tags', 'author', 'image', 'published_at', 'is_published', 'created_at', 'updated_at']
