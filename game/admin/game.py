from django.contrib import admin

from game.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("id", "started", "winner")
    search_fields = ["id"]
