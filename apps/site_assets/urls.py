from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SiteAssetViewSet

router = DefaultRouter()
router.register(r'recursos', SiteAssetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]