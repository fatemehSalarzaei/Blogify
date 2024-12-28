from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Tag, Post, Comment, Bookmark, Like
from .serializers import CategorySerializer, TagSerializer, PostSerializer, CommentSerializer, BookmarkSerializer, LikeSerializer
import django_filters

class PostFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    created_at = django_filters.DateFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Post
        fields = ['category', 'created_at']

# Admin Views

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]
    search_fields = ['title', 'content', 'category__name', 'tags__name']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)

class CommentAdminViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]
    search_fields = ['content', 'post__title']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_fields = ['post']

class BookmarkAdminViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAdminUser]

class LikeAdminViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAdminUser]

# User Views

class PostUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    search_fields = ['title', 'content', 'category__name', 'tags__name']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_class = PostFilter

class CommentUserViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(is_approved=True)
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['content', 'post__title']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookmarkUserViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.filter(user=self.request.user)
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeUserViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.filter(user=self.request.user)
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
