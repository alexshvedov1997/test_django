from rest_framework import serializers
from contracts.custom_models.contract import Contracts, ContractsApplication
from contracts.custom_models.products import Products
from datetime import datetime
from contracts.utils.constants import DATETIME_FORMAT


class ContractsSerializers(serializers.Serializer):
    contract_number = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=5000)
    products = serializers.ListField(child=serializers.CharField())

    def create(self, validated_data):
        contract_number = validated_data.get("contract_number")
        description = validated_data.get("description")
        product_names = validated_data.get("products", [])
        product_ids = list(Products.objects.filter(name__in=product_names).values_list("id", flat=True))
        contract_id = Contracts.objects.create(
            contract_number=contract_number,
            description=description,
        )
        contract_application_id = ContractsApplication.objects.create(
            application_number=self.generate_application_number(contract_id),
            contract_application_id=contract_id,

        )
        contract_application_id.product_ids.add(*product_ids)
        return contract_id

    def generate_application_number(self, contract_id):
        contract_date = contract_id.created.strftime(DATETIME_FORMAT)
        contract_number = contract_id.contract_number
        return f"{contract_date} - {contract_number}"
