from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, ProjectTechnology, Project, ProjectMedia
from .serializers import CategorySerializer, ProjectTechnologySerializer, ProjectSerializer, ProjectMediaSerializer




# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProjectTechnologyViewSet(viewsets.ModelViewSet):
    queryset = ProjectTechnology.objects.all()
    serializer_class = ProjectTechnologySerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectMediaViewSet(viewsets.ModelViewSet):
    queryset = ProjectMedia.objects.all()
    serializer_class = ProjectMediaSerializer
    
