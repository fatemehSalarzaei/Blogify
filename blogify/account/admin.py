from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Author

class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'bio', 'profile_picture', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    list_display = ('email', 'username', 'is_active', 'is_staff', 'is_superuser', 'created_at')
    search_fields = ('email', 'username')
    ordering = ('email',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'expertise', 'website')
    search_fields = ('user__username', 'expertise', 'website')
    list_filter = ('user__is_active',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Author, AuthorAdmin)
