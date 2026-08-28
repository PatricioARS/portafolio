from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProjectTechnologyViewSet, ProjectViewSet, ProjectMediaViewSet


router = DefaultRouter()
router.register(r'categorias', CategoryViewSet)
router.register(r'tecnologias', ProjectTechnologyViewSet)
router.register(r'proyectos', ProjectViewSet)
router.register(r'galeria', ProjectMediaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    
]