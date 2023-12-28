from rest_framework import serializers
from contracts.custom_models.products import Brands, Products


class BrandsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brands
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ["name", "brand_id", "description"]
