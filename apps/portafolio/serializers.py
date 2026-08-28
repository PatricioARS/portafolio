from rest_framework import serializers
from .models import Category, ProjectTechnology, Project, ProjectMedia

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProjectTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTechnology
        fields = ['id', 'name', 'icon_slug']


class ProjectMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMedia
        fields = ['id', 'image_url', 'caption', 'display_order', 'aspect_ratio']


class ProjectSerializer(serializers.ModelSerializer):
    # Traducimos las relaciones completas para que el JSON entregue el objeto traducido de la categoría, tecnologías y galería
    category = CategorySerializer(read_only=True)
    technologies = ProjectTechnologySerializer(many=True, read_only=True)
    media_gallery = ProjectMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'summary', 'description', 
            'image', 'featured', 'project_url', 'created_at',
            'category', 'technologies', 'media_gallery'
        ]