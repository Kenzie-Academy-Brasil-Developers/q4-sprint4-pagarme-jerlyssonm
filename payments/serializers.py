from rest_framework import serializers
from .models import PaymentInfo


class PaymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInfo
        fields = "__all__"

        extra_kwargs = {
            "is_active": {"read_only": True},
        }

    def create(self, validated_data):
        request = self.context["request"]

        return PaymentInfo.objects.create(**validated_data, customer=request.user)