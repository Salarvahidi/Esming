from rest_framework import serializers

from game.models import Game


class GameSerializer(serializers.ModelSerializer):
    model = Game
    fields = "__all__"

    def to_representation(self, instance):
        from user.serializers import MiniUserSerializer
        from game.serializers import RoundResultSerializer

        res = super().to_representation(instance)
        res["winner"] = MiniUserSerializer(data=instance.winner).data
        res["room"] = instance.room.name
        res["result"] = RoundResultSerializer(
            data=instance.round_result, many=True
        ).data
        return res
