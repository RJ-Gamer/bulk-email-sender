"""
url configuration for authentication app
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authentication.views.login import LoginViewSet


router = DefaultRouter()

router.register("login", LoginViewSet, basename="login")

urlpatterns = [
    path("users/", include(router.urls)),
]
