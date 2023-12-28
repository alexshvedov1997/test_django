from django.urls import path, include
from contracts.api.v1.product_viewsets import BrandsViewSet

app_name = "contracts_urls"

urlpatterns = [
    path("api/v1/", include("contracts.api.v1.urls")),
]
