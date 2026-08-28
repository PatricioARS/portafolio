from django.db import models

# Create your models here.

class Profile(models.Model):
    # CharField = Texto corto con un límite de caracteres (max_length)
    fullname = models.CharField(max_length=100, verbose_name="Nombre Completo")
    headline = models.CharField(max_length=150, verbose_name="Titular / Profesión")
    
    # TextField = Texto largo sin límite rígido (para biografías)
    bio = models.TextField(verbose_name="Biografía / Sobre Mí")
    
    # Reemplazamos avatar_url por un ImageField seguro
    avatar = models.ImageField(upload_to='perfiles/', null=True, blank=True)
    cv_url = models.URLField(max_length=255, blank=True, null=True, verbose_name="URL del CV (PDF)")
    avatar_3d = models.ImageField(upload_to='perfiles/', null=True, blank=True)
    
    # BooleanField = Campo verdadero/falso (1 o 0)
    is_active = models.BooleanField(default=True, verbose_name="¿Perfil Activo?")

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return f"{self.fullname} - {self.headline}"


class SocialLink(models.Model):
    # ForeignKey = Clave Foránea. Relaciona este enlace con un Perfil específico.
    # ON_DELETE CASCADE = Si se borra el Perfil, se borran automáticamente sus redes sociales.
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='social_links')
    
    platform = models.CharField(max_length=50, verbose_name="Plataforma (Ej: LinkedIn)")
    url = models.URLField(max_length=255, verbose_name="Enlace Red Social")
    icon_name = models.CharField(max_length=50, verbose_name="Nombre Icono")

    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"

    def __str__(self):
        return f"{self.platform} ({self.profile.fullname})"