from rest_framework import serializers
from .models import Category, Tag, Post, Comment, Bookmark, Like

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'



class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'tags', 'image', 'published_at', 'is_published', 'created_at', 'updated_at', 'author']
        read_only_fields = ['author']  

    def create(self, validated_data):
        user = self.context['request'].user

        post = Post.objects.create(
            author=user.author,  
            **validated_data
        )

        return post

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'created_at', 'is_approved']


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'post', 'user', 'created_at']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at']
