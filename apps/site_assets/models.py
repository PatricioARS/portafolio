from django.db import models

# Create your models here.

class SiteAsset(models.Model):
    key = models.CharField(max_length=50, unique=True, verbose_name="Clave Única (Ej: hero_logo)")
    title = models.CharField(max_length=100, verbose_name="Título del Recurso")
    asset_url = models.ImageField(upload_to='assets/', null=True, blank=True)
    description = models.TextField(blank=True, null=True, verbose_name="Descripción Corta")

    class Meta:
        verbose_name = "Recurso del Sitio"
        verbose_name_plural = "Recursos del Sitio"

    def __str__(self):
        return f"{self.title} ({self.key})"