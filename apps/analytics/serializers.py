from rest_framework import serializers
from .models import BiDataset, BiMetric

class BiMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiMetric
        fields = ['id', 'group_name', 'label', 'numeric_value', 'filter_tag']


class BiDatasetSerializer(serializers.ModelSerializer):
    # Anidamos las métricas pertenecientes a este Dataset específico
    metrics = BiMetricSerializer(many=True, read_only=True)

    class Meta:
        model = BiDataset
        fields = [
            'id', 'project', 'title', 'total_respondents', 
            'description', 'cv_url', 'is_active', 'metrics'
        ]