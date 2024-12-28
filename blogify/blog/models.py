from django.db import models
from django.utils import timezone
from account.models import Author , CustomUser

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        'self',
        related_name='subcategories',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)  
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        related_name='posts',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        Author,
        related_name='posts',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    image = models.ImageField(upload_to='posts/images/', null=True, blank=True)
    is_published = models.BooleanField(default=False)
    meta_title = models.CharField(max_length=255, blank=True, null=True)  
    meta_description = models.TextField(blank=True, null=True)  
    published_at = models.DateTimeField(default=timezone.now)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-published_at']  

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        CustomUser,
        related_name='comments',
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'



class Bookmark(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='bookmarks',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        CustomUser,
        related_name='bookmarks',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} bookmarked {self.post.title}'


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='likes',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        CustomUser,
        related_name='likes',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} liked {self.post.title}'