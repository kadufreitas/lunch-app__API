from rest_framework import serializers

from app.models import *


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('id', 'name', 'bank')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'value', 'photo', 'sellers')


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id', 'value', 'products', 'client', 'seller', 'paid')
