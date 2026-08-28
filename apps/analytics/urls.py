from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BiDatasetViewSet, BiMetricViewSet
from . import views

router = DefaultRouter()
router.register(r'datasets', BiDatasetViewSet)
router.register(r'metricas', BiMetricViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/finanzas/', views.obtener_datos_financieros, name='api_finanzas'),
    path('api/oportunidad-etf/', views.indice_oportunidad_etf, name='api_oportunidad'),
]