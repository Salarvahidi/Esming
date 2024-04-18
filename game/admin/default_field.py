from django.contrib import admin

from game.models import DefaultField


@admin.register(DefaultField)
class DefaultFieldAdmin(admin.ModelAdmin):
    list_display = ("id", "field_name", "is_active")
    search_fields = ["field_name"]
