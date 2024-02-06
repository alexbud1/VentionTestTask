from django.urls import path
from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

router = SimpleRouter()


router.register(r"category", views.CategoryViewSet, basename="category")
router.register(r"task", views.TaskViewSet, basename="task")

appname = "api"

urlpatterns = router.urls + [
    path(r'refresh-login/', TokenRefreshView.as_view(), name='user_refresh_token_login'),
    path(r'login/', TokenObtainPairView.as_view(), name='user_credentials_login'),
    path(r'register/', views.RegisterView.as_view(), name='register'),
]