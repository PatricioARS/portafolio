from django.shortcuts import render
from rest_framework import viewsets
from .models import SiteAsset
from .serializers import SiteAssetSerializer

# Create your views here.

class SiteAssetViewSet(viewsets.ModelViewSet):
    queryset = SiteAsset.objects.all()
    serializer_class = SiteAssetSerializer