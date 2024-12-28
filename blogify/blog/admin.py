from django.contrib import admin
from .models import Category, Tag, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    prepopulated_fields = {"name": ("parent",)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_published', 'published_at', 'created_at')
    search_fields = ('title', 'content', 'author__name')
    list_filter = ('is_published', 'category', 'tags', 'created_at', 'published_at')
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ['author', 'category', 'tags']
    date_hierarchy = 'published_at'
    ordering = ('-published_at',)
    filter_horizontal = ('tags',)
    fieldsets = (
        ('General Information', {
            'fields': ('title', 'slug', 'content', 'image', 'category', 'tags', 'author')
        }),
        ('Publication Status', {
            'fields': ('is_published', 'published_at')
        }),
        ('Meta Information', {
            'fields': ('meta_title', 'meta_description')
        }),
    )
