from django.contrib import admin

from account.models import *

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'created_at') 
    search_fields = ('username', 'email', 'full_name') 
    list_filter = ('is_active', 'is_staff', 'created_at')  

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_email', 'get_username', 'bio') 
    search_fields = ('user__username', 'user__email', 'bio') 
    list_filter = ('user__is_active', )  
    autocomplete_fields = ('user',)  

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'