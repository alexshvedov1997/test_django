from django.contrib import admin


class AdminBrands(admin.ModelAdmin):
    list_display = ["name", "created"]
    ordering = ("-created",)


class AdminProducts(admin.ModelAdmin):
    list_display = ("name", "created", "brand_id")
    search_fields = ("title", "brand_id__name")
    ordering = ("-created",)
