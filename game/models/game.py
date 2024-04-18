from django.db import models
from django.utils.translation import gettext_lazy as _


class Game(models.Model):
    room = models.ForeignKey(
        "game.Room",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_("room"),
    )
    round_result = models.ManyToManyField(
        "game.RoundResult",
        blank=True,
        related_name="games",
        verbose_name=_("round result"),
    )
    winner = models.ForeignKey(
        "user.User", on_delete=models.SET_NULL, null=True, verbose_name=_("winner")
    )
    fields = models.ManyToManyField(
        "game.DefaultField",
        blank=True,
        related_name="games",
        verbose_name=_("default field"),
    )
    started = models.DateTimeField(
        auto_now=False, auto_now_add=True, verbose_name=_("started")
    )
    is_finished = models.BooleanField(default=False, verbose_name=_("is finished"))

    def __str__(self) -> str:
        return f"winner : {self.winner.username}" if self.winner else ""

    class Meta:
        verbose_name = _("game")
        verbose_name_plural = _("games")
