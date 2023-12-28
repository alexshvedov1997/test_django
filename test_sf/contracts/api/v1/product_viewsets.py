from rest_framework import viewsets
from contracts.custom_models.products import Brands, Products
from .product_serializers import BrandsSerializer, ProductSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Brands"])
class BrandsViewSet(viewsets.ModelViewSet):

    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer


@extend_schema(tags=["Products"])
class ProductsViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer
