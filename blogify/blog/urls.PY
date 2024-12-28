from rest_framework.routers import DefaultRouter
from .views import PostAdminViewSet, CommentAdminViewSet, BookmarkAdminViewSet, LikeAdminViewSet, PostUserViewSet, CommentUserViewSet, BookmarkUserViewSet, LikeUserViewSet

router = DefaultRouter()

router.register(r'admin/posts', PostAdminViewSet, basename='admin-post')
router.register(r'admin/comments', CommentAdminViewSet, basename='admin-comment')
router.register(r'admin/bookmarks', BookmarkAdminViewSet, basename='admin-bookmark')
router.register(r'admin/likes', LikeAdminViewSet, basename='admin-like')

router.register(r'posts', PostUserViewSet, basename='post')
router.register(r'comments', CommentUserViewSet, basename='comment')
router.register(r'bookmarks', BookmarkUserViewSet, basename='bookmark')
router.register(r'likes', LikeUserViewSet, basename='like')

urlpatterns = router.urls
