from rest_framework import viewsets

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
