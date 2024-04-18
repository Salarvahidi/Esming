from rest_framework import serializers

from game.models import Game, RoundResult
from game.serializers import RoundResultSerializer


class GameSerializer(serializers.ModelSerializer):
    round_result = RoundResultSerializer(many=True, required=True)

    class Meta:
        model = Game
        fields = "__all__"

    def to_representation(self, instance):
        from user.serializers import MiniUserSerializer

        res = super().to_representation(instance)
        res["winner"] = MiniUserSerializer(instance.winner).data
        res["room"] = instance.room.room_name if instance.room else ""
        return res
