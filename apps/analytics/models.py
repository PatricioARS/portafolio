from django.db import models

# Create your models here.

class BiDataset(models.Model):
    # Relación entre Apps: Conectamos con el modelo Project de la app portafolio
    # SET_NULL: Si borras el proyecto, el Dataset de BI NO se borra, solo se desvincula (queda null)
    project = models.ForeignKey(
        'portafolio.Project', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='bi_datasets',
        verbose_name="Proyecto Asociado"
    )
    title = models.CharField(max_length=100, verbose_name="Título del Dataset")
    total_respondents = models.IntegerField(default=0, verbose_name="Total Encuestados")
    description = models.TextField(verbose_name="Descripción / Metodología")
    cv_url = models.URLField(max_length=255, blank=True, null=True, verbose_name="URL Documentación Extra")
    is_active = models.BooleanField(default=True, verbose_name="¿Dataset Activo?")

    class Meta:
        verbose_name = "Dataset de BI"
        verbose_name_plural = "Datasets de BI"

    def __str__(self):
        return self.title


class BiMetric(models.Model):
    # Relación: Cada métrica pertenece a 1 Dataset específico de BI
    dataset = models.ForeignKey(BiDataset, on_delete=models.CASCADE, related_name='metrics', verbose_name="Dataset")
    
    group_name = models.CharField(max_length=50, verbose_name="Nombre del Grupo (Ej: Asignatura Preferida)")
    label = models.CharField(max_length=100, verbose_name="Etiqueta (Ej: Matemáticas)")
    
    # DecimalField: Guarda números con decimales exactos (ideal para porcentajes o indicadores de BI)
    numeric_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Numérico / Porcentaje")
    filter_tag = models.CharField(max_length=50, blank=True, null=True, verbose_name="Filtro (Ej: 7mo Basico)")

    class Meta:
        verbose_name = "Métrica de BI"
        verbose_name_plural = "Métricas de BI"

    def __str__(self):
        return f"{self.group_name} - {self.label}: {self.numeric_value}"