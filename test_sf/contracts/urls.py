from django.urls import path, include

app_name = "contracts_urls"

urlpatterns = [
    path("api/v1/", include("contracts.api.v1.urls")),
]
