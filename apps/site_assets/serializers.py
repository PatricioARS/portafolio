from rest_framework import serializers
from .models import SiteAsset

class SiteAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteAsset
        fields = ['id', 'key', 'title', 'asset_url', 'description']