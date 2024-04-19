from rest_framework import serializers

from game.models import RoundResult
from game.helpers.validator import check_values, score


class RoundResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoundResult
        fields = "__all__"

    def validate(self, attrs):
        check = check_values(attrs["data"])
        data = score(attrs["letter"], check, attrs["data"])
        for each in data:
            each["total_point"] = sum([val[1] for _, val in each["values"].items()])
        attrs["data"] = data
        return super().validate(attrs)
