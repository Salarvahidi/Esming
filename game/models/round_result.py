from django.db import models
from django.utils.translation import gettext_lazy as _


def default_data():
    return {}


class RoundResult(models.Model):
    game = models.ForeignKey(
        "game.Game",
        on_delete=models.CASCADE,
        related_name="round_result",
        blank=True,
        null=True,
        verbose_name="game",
    )
    letter = models.CharField(max_length=1, verbose_name=_("Letter"))
    data = models.JSONField(default=default_data)

    class Meta:
        verbose_name = _("round result")
        verbose_name_plural = _("round results")
