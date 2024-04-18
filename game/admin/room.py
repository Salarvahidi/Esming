from django.contrib import admin

from game.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "room_name", "created_at")
    search_fields = ["id"]
