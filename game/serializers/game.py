from rest_framework import serializers

from game.models import Game, RoundResult


class GameSerializer(serializers.ModelSerializer):
    class Meta:
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

    def _result_bulk_create(self, result: list):
        bulk_result = []
        for data in result:
            bulk_result.append(
                RoundResult(
                    letter=data["letter"],
                    data=data["data"],
                    round_count=data["round_count"],
                )
            )
        RoundResult.objects.bulk_create(bulk_result)

    def create(self, validated_data):
        results = validated_data.pop("round_result")
        game = super().create(validated_data)
        self._result_bulk_create(results)
        return game
