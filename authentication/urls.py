"""
url configuration for authentication app
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authentication.views import LoginViewSet, UserViewSet


router = DefaultRouter()

router.register("login", LoginViewSet, basename="login")
router.register("user", UserViewSet, basename="user")

urlpatterns = [
    path("users/", include(router.urls)),
]
