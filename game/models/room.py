from django.db import models
from django.utils.translation import gettext_lazy as _


class Room(models.Model):
    room_name = models.CharField(
        max_length=100, blank=True, verbose_name=_("room name")
    )
    leader = models.ForeignKey(
        "user.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="leader_room",
        verbose_name=_("leader"),
    )
    players = models.ManyToManyField(
        "user.User",
        blank=True,
        verbose_name=_("players"),
        related_name="room_players",
    )
    created_at = models.DateTimeField(
        auto_now=False, auto_now_add=True, verbose_name=_("created at")
    )

    def __str__(self):
        return self.room_name if not None else ""

    class Meta:
        verbose_name = _("room")
        verbose_name_plural = _("rooms")
