from rest_framework import serializers

from game.models import RoundResult


class RoundResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoundResult
        fields = "__all__"
