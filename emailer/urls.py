"""
url configuration for emailer app
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmailTemplateViewSet, EmailValidatorViewSet, BulkEmailerViewSet

router = DefaultRouter()

router.register("email-templates", EmailTemplateViewSet, basename="email-templates")
router.register("email-validator", EmailValidatorViewSet, basename="email-validator")
router.register("bulk-emailer", BulkEmailerViewSet, basename="bulk-emailer")

urlpatterns = [
    path("emailer/", include(router.urls)),
]
