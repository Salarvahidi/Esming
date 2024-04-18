from django.db import models
from django.utils.translation import gettext_lazy as _


def default_data():
    return {}


class RoundResult(models.Model):
    letter = models.CharField(max_length=1, verbose_name=_("Letter"))
    data = models.JSONField(default=default_data)
    round_count = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_("round count")
    )
