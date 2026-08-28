from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, SocialLinkViewSet

# El Router se encarga de generar todas las sub-rutas de forma automática
router = DefaultRouter()
router.register(r'usuarios', ProfileViewSet)
router.register(r'redes-sociales', SocialLinkViewSet)

# urlpatterns es una lista de Python que Django lee para entender la navegación
urlpatterns = [
    path('', include(router.urls)),
]