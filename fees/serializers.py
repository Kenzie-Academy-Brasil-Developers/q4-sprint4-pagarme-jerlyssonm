from rest_framework import serializers
from .models import Fees


class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fees
        fields = "__all__"

        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
        }

    def validate(self, attrs):
        if attrs["credit_fee"] < 0:
            attrs["credit_fee"] = 0
        if attrs["debit_fee"] < 0:
            attrs["debit_fee"] = 0
        return super().validate(attrs)

    def create(self, validated_data):

        return Fees.objects.create(**validated_data)