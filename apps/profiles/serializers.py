from rest_framework import serializers
from .models import Profile, SocialLink

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ['id', 'platform', 'url', 'icon_name']


class ProfileSerializer(serializers.ModelSerializer):
    # Incluimos las redes sociales anidadas dentro del perfil usando su related_name ('social_links')
    social_links = SocialLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'fullname', 'headline', 'bio', 'avatar', 'avatar_3d', 'cv_url', 'is_active', 'social_links']