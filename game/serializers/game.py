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

    def _result_bulk_create(self, game: Game, round_result):
        bulk_result = []
        for data in round_result:
            bulk_result.append(
                RoundResult(
                    game=game,
                    letter=data["letter"],
                    data=data["data"],
                    round_count=data["round_count"],
                )
            )
        RoundResult.objects.bulk_create(bulk_result)

    def create(self, validated_data):
        round_result = validated_data.pop("round_result", [])
        game = super().create(validated_data)
        self._result_bulk_create(game, round_result)
        return game
