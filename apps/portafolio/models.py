from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre Categoría")
    # SlugField = Texto en minúsculas separado por guiones ideal para las URLs
    slug = models.SlugField(max_length=50, unique=True, verbose_name="Slug (URL)")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class ProjectTechnology(models.Model):
    name = models.CharField(max_length=50, verbose_name="Tecnología (Ej: Django, Vue 3)")
    icon_slug = models.CharField(max_length=50, verbose_name="Identificador Icono")

    class Meta:
        verbose_name = "Tecnología"
        verbose_name_plural = "Tecnologías"

    def __str__(self):
        return self.name


class Project(models.Model):
    # Relación muchos a uno: Cada proyecto pertenece a 1 categoría
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects', verbose_name="Categoría")
    
    # Relación muchos a muchos: Un proyecto usa varias tecnologías y una tecnología está en varios proyectos
    technologies = models.ManyToManyField(ProjectTechnology, related_name='projects', verbose_name="Tecnologías Usadas")
    
    title = models.CharField(max_length=150, verbose_name="Título del Proyecto")
    slug = models.SlugField(max_length=150, unique=True, verbose_name="Slug")
    summary = models.TextField(verbose_name="Resumen Corto")
    description = models.TextField(verbose_name="Descripción Detallada")
    image = models.ImageField(upload_to='proyectos/', null=True, blank=True)
    featured = models.BooleanField(default=False, verbose_name="¿Proyecto Destacado?")
    project_url = models.URLField(max_length=255, blank=True, null=True, verbose_name="Enlace Demo")
    
    # DateTimeField auto_now_add = Guarda automáticamente la fecha y hora exacta de creación
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ProjectMedia(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='media_gallery', verbose_name="Proyecto")
    image_url = models.URLField(max_length=255, verbose_name="URL Imagen Galería")
    caption = models.CharField(max_length=150, blank=True, null=True, verbose_name="Pie de Foto")
    
    # IntegerField = Para números enteros (orden de visualización en el frontend)
    display_order = models.IntegerField(default=0, verbose_name="Orden de Visualización")
    aspect_ratio = models.CharField(max_length=20, default='landscape', verbose_name="Relación Aspecto")

    class Meta:
        verbose_name = "Galería del Proyecto"
        verbose_name_plural = "Galerías de Proyectos"
        ordering = ['display_order']

    def __str__(self):
        return f"Imagen de {self.project.title}"