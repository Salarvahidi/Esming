from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ("is_superuser", "last_login", "date_joined")
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 6, "required": False}
        }

    def create(self, validated_data):
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)


class MiniUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "last_name", "first_name"]
