from rest_framework import serializers
from products.models import Products
from users.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'description', 'price', 'quantity', 'is_active', 'seller']
        depth = 1
  
    def create(self, validated_data):
        seller = self.context['request'].user
        return Products.objects.create(**validated_data, seller=seller)
