from django.contrib import admin
from game.models import RoundResult


@admin.register(RoundResult)
class RoundResultAdmin(admin.ModelAdmin):
    list_display = ("id", "game_id", "letter")

    def game_id(self, obj):
        return obj.game.id
