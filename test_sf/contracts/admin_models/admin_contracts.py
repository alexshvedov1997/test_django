from django.contrib import admin
from contracts.custom_models.products import Products
from django.utils.translation import gettext_lazy as _


class ProductsInline(admin.TabularInline):
    extra = 0
    model = Products


class AdminContracts(admin.ModelAdmin):
    list_display = ("contract_number", "created")


class AdminContractApplication(admin.ModelAdmin):
    inline = [ProductsInline]
    list_display = ("application_number", "contract_application_id", "created", "get_products")
    ordering = ("-created",)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("product_ids")

    def get_products(self, obj):
        return ',\n'.join([product.name for product in obj.product_ids.all()[:5]])

    get_products.short_description = _("Products")
