from django.db import models
from django.utils.translation import gettext_lazy as _


class DefaultField(models.Model):
    field_name = models.CharField(
        max_length=100, blank=True, verbose_name=_("field name")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("is active"))

    def __str__(self):
        return self.field_name if not None else ""

    class Meta:
        verbose_name = _("default_field")
        verbose_name_plural = _("default_fields")
