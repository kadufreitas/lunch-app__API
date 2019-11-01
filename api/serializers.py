from functools import reduce

from django.shortcuts import redirect
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

    def save(self, *args, **kwargs):
        self.validated_data['value'] = sum(
            [product.value for product in self.validated_data['products']]
        )
        super().save(*args, **kwargs)

    products = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        many=True,
        write_only=True
    )
    products_names = serializers.StringRelatedField(source='products', read_only=True, many=True)
    client_name = serializers.StringRelatedField(source='client', read_only=True)
    seller_name = serializers.StringRelatedField(source='seller', read_only=True)

    class Meta:
        model = Sale
        fields = (
        'id', 'value', 'products', 'client', 'products_names', 'client_name',
        'seller_name', 'seller', 'paid')
        read_only_fields = ['value']
        extra_kwargs = {
            'products': {
                'write_only': True
            },
            'client': {
                'write_only': True
            },
            'seller': {
                'write_only': True
            },
        }
        # read_only_fields = ['value', 'paid']
