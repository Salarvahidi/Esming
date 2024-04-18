from rest_framework import serializers

from game.models import DefaultField


class DefaultFieldSerializer(serializers.ModelSerializer):
    model = DefaultField
    fields = "__all__"
