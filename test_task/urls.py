from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Test Task API",
        default_version='v1',
        description="Documentation for the Test Task API for Vention",
        contact=openapi.Contact(email="alexbud1.dev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path(r'docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
