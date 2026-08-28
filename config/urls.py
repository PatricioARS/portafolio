"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

#--- IMPORTACIONES PARA SWAGGER ---
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# --- CONFIGURACIÓN VISUAL DE SWAGGER ---
schema_view = get_schema_view(
   openapi.Info(
      title="API Portafolio Profesional",
      default_version='v1',
      description="Documentación oficial e interactiva del Backend de mi Portafolio.",
      contact=openapi.Contact(email="correo@ejemplo.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny], # Permitimos que cualquiera vea el manual
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- RUTA DE LA DOCUMENTACIÓN ---
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # --- RUTAS DE SEGURIDAD Y LOGIN (JWT) ---
    path('api/v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # --- RUTAS DE NUESTRAS APPS ---
    path('api/v1/profiles/', include('apps.profiles.urls')),
    path('api/v1/portafolio/', include('apps.portafolio.urls')),
    path('api/v1/analytics/', include('apps.analytics.urls')),
    path('api/v1/site-assets/', include('apps.site_assets.urls')),
]
# Le dice a Django cómo mostrar los archivos en la ruta /media/
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)