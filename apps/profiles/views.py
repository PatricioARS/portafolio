from rest_framework import viewsets
from .models import Profile, SocialLink
from .serializers import ProfileSerializer, SocialLinkSerializer

# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    # 1. queryset: Le dice al camarero dónde buscar los datos en MySQL
    queryset = Profile.objects.all()
    # 2. serializer_class: Le dice qué traductor usar
    serializer_class = ProfileSerializer

class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer