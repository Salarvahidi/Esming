from rest_framework import serializers

from game.models import Room


class RoomSerializer(serializers.ModelSerializer):
    model = Room
    fields = "__all__"

    def to_representation(self, instance):
        from user.serializers import MiniUserSerializer

        res = super().to_representation(instance)
        res["leader"] = MiniUserSerializer(data=instance.leader).data
        res["players"] = MiniUserSerializer(data=instance.players, many=True).data

        return res
