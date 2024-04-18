from rest_framework import serializers

from game.models import DefaultField


class DefaultFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultField
        fields = "__all__"
