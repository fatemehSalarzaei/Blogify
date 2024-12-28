from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostAdminViewSet, CommentAdminViewSet, BookmarkAdminViewSet, LikeAdminViewSet,
    PostUserViewSet, CommentUserViewSet, BookmarkUserViewSet, LikeUserViewSet
)

router_admin = DefaultRouter()
router_admin.register(r'posts', PostAdminViewSet)
router_admin.register(r'comments', CommentAdminViewSet)
router_admin.register(r'bookmarks', BookmarkAdminViewSet)
router_admin.register(r'likes', LikeAdminViewSet)

router_user = DefaultRouter()
router_user.register(r'posts', PostUserViewSet)
router_user.register(r'comments', CommentUserViewSet)
router_user.register(r'bookmarks', BookmarkUserViewSet)
router_user.register(r'likes', LikeUserViewSet)

urlpatterns = [
    path('admin/', include(router_admin.urls)),
    path('user/', include(router_user.urls)),
]
