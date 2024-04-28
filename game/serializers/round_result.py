from rest_framework import serializers

from game.models import RoundResult
from game.helpers.validator import check_values, score


class RoundResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoundResult
        fields = "__all__"

    def validate(self, attrs):
        check = check_values(attrs["data"])
        data, zero = score(attrs["letter"], check, attrs["data"])
        for each in data:
            each["total_point"] = 0
            for key, val in each["values"].items():
                for item in zero:
                    if not each["user"] in item.keys() and key in item.values():
                        val[1] += 10
                each["total_point"] += val[1]
        attrs["data"] = data
        return super().validate(attrs)
