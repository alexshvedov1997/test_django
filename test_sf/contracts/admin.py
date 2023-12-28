from django.contrib import admin
from contracts.custom_models.products import Products, Brands
from contracts.custom_models.contract import Contracts, ContractsApplication
from contracts.admin_models.admin_products import AdminProducts, AdminBrands
from contracts.admin_models.admin_contracts import AdminContractApplication, AdminContracts


admin.site.register(Products, AdminProducts)
admin.site.register(Brands, AdminBrands)
admin.site.register(Contracts, AdminContracts)
admin.site.register(ContractsApplication, AdminContractApplication)
