from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include('admin_portal.urls')), 
    path('user/', include('user_portal.urls')), 
    path('accounts/', include('account.urls')), 
    path('blog/', include('blog.urls')),        
]
