from django.db import models
from django.utils.translation import gettext_lazy as _
from contracts.custom_models.mixins import TimeStampedMixin


class Brands(TimeStampedMixin):

    name = models.CharField(verbose_name=_("Brand name"), max_length=255, unique=True)

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return self.name


class Products(TimeStampedMixin):

    name = models.CharField(verbose_name=_("Product name"), max_length=255, unique=True)
    description = models.TextField(verbose_name=_("Description"), blank=True)
    brand_id = models.ForeignKey(
        to=Brands,
        on_delete=models.CASCADE,
        related_name="product_ids",
    )

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name
