from django.db import models
from django.utils.translation import gettext_lazy as _


class DefaultField(models.Model):
    field_name = models.CharField(max_length=100, verbose_name=_("field name"))
    is_active = models.BooleanField(default=True, verbose_name=_("is active"))

    def __str__(self):
        return self.field_name

    class Meta:
        verbose_name = _("field name")
        verbose_name_plural = _("field names")
