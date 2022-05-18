from rest_framework import serializers
from products.models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'description', 'price', 'quantity', 'is_active', 'seller']
        depth = 1

    def validate(self, attrs):
        if attrs["price"] < 0:
            attrs["price"] = 0
        if attrs["quantity"] <= 0:
            attrs["quantity"] = 1
        return super().validate(attrs)

    def create(self, validated_data):
        seller = self.context['request'].user
        return Products.objects.create(**validated_data, seller=seller)

class ProductPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("description", "price", "quantity", "is_active", "is_seller" )

        extra_kwargs = {
            "description": {"required": False},
            "price": {"required": False},
            "quantity": {"required": False},
            "is_active": {"required": False}, 
        }
