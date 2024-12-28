from django.db import models
from django.utils import timezone
from account.models import Author

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
