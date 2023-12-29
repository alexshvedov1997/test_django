from django.contrib import admin

from contracts.admin_models.admin_contracts import (
    AdminContractApplication,
    AdminContracts,
)
from contracts.admin_models.admin_products import AdminBrands, AdminProducts
from contracts.custom_models.contract import Contracts, ContractsApplication
from contracts.custom_models.products import Brands, Products

admin.site.register(Products, AdminProducts)
admin.site.register(Brands, AdminBrands)
admin.site.register(Contracts, AdminContracts)
admin.site.register(ContractsApplication, AdminContractApplication)
