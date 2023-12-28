from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(_('Created date'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified date'), auto_now=True)

    class Meta:
        abstract = True
