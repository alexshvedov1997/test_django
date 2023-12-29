from contracts.custom_models.mixins import TimeStampedMixin
from contracts.custom_models.products import Products
from django.db import models
from django.utils.translation import gettext_lazy as _


class Contracts(TimeStampedMixin):
    contract_number = models.CharField(
        verbose_name=_("Contract number"),
        max_length=255,
        unique=True,
    )
    description = models.TextField(verbose_name=_("Description"), blank=True)

    def __str__(self):
        return self.contract_number

    class Meta:
        verbose_name = _('Contract')
        verbose_name_plural = _('Contracts')


class ContractsApplication(TimeStampedMixin):

    application_number = models.CharField(
        verbose_name=_("Application number"),
        max_length=255,
        unique=True,
    )
    product_ids = models.ManyToManyField(
        to=Products,
        related_name="contract_application_ids"
    )
    contract_application_id = models.OneToOneField(
        to=Contracts,
        on_delete=models.DO_NOTHING,
        related_name="contract_application_id",
    )

    def __str__(self):
        return self.application_number

    class Meta:
        verbose_name = _('Contract application')
        verbose_name_plural = _('Contracts Application')
