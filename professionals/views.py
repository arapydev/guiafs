from rest_framework import viewsets
from .models import Category, Professional
from .serializers import CategorySerializer, ProfessionalSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint que permite ver las categorías.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProfessionalViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint que permite ver los profesionales.
    """
    queryset = Professional.objects.all().order_by('full_name')
    serializer_class = ProfessionalSerializer