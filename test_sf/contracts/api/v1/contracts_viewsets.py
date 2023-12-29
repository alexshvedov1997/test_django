from contracts.api.v1.contracts_serializers import ContractsSerializers
from contracts.custom_models.contract import ContractsApplication
from django.db.models import F
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.response import Response


@extend_schema(tags=["Contracts"])
class ContractsViewsCreate(generics.CreateAPIView):
    serializer_class = ContractsSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "Contract executed successfully."}, status=status.HTTP_201_CREATED)


@extend_schema(tags=["Contracts"])
class ContractsProductsViews(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        contract_id = self.kwargs.get(self.lookup_field)
        product_names = ContractsApplication.objects.select_related(
            "contract_application_id",
            "product_ids",
        ).filter(
            contract_application_id__id=contract_id,
        ).annotate(
           product_name=F("product_ids__name"),
        ).values("product_name")
        return Response(product_names, status=status.HTTP_200_OK)
