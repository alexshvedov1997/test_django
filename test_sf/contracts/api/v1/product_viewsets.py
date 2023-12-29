from contracts.custom_models.products import Brands, Products
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from .product_serializers import BrandsSerializer, ProductSerializer


@extend_schema(tags=["Brands"])
class BrandsViewSet(viewsets.ModelViewSet):

    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer


@extend_schema(tags=["Products"])
class ProductsViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer
