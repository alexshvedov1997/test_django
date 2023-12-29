from contracts.api.v1.contracts_viewsets import (ContractsProductsViews,
                                                 ContractsViewsCreate)
from contracts.api.v1.product_viewsets import BrandsViewSet, ProductsViewSet
from django.urls import path

urlpatterns = [
    path("brands/", BrandsViewSet.as_view({'post': 'create'})),
    path("brands/<int:pk>", BrandsViewSet.as_view({'get': 'retrieve'})),
    path("products/", ProductsViewSet.as_view({'post': 'create'})),
    path("products/<int:pk>", ProductsViewSet.as_view({'get': 'retrieve'})),
    path("contracts/", ContractsViewsCreate.as_view()),
    path("contracts/<int:pk>/", ContractsProductsViews.as_view()),
]
