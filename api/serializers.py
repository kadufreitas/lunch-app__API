from rest_framework import serializers

from app.models import Seller, Client, Product, Sale


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('id', 'name', 'bank')

class SellerSerializerRelation(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    class Meta:
        model = Seller
        fields = ('id', 'name')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name')



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'value', 'photo', 'sellers')

class ProductSerializerDetail(serializers.ModelSerializer):
    sellers = SellerSerializerRelation(many=True, read_only=True)
    name = serializers.CharField(read_only=True)
    value = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
    photo = serializers.ImageField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'value', 'photo', 'sellers')


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id', 'value', 'products', 'client', 'seller', 'paid')
