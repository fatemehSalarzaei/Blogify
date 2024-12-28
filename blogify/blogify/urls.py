from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Blogify API",
        default_version='v1',
        description="API documentation for Blogify project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@blogify.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

urlpatterns = [
    path('swagger/', schema_view.as_view(), name='swagger'),
    # path('accounts/', include('account.urls')), 
    path('blog/', include('blog.urls')),        
]
