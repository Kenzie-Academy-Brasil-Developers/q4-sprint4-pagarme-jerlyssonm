from rest_framework import serializers
from .models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_admin",
            "is_seller",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
            "is_admin":{"default": False},
            "is_seller": {"default": False},
        }


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()