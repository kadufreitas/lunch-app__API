from rest_framework.viewsets import ModelViewSet
from rest_framework.schemas.openapi import AutoSchema
import coreapi

from app.models import Seller, Client, Product, Sale
from .serializers import (
    SellerSerializer,
    ClientSerializer,
    ProductSerializer,
    ProductSerializerDetail,
    SaleSerializer,
)


class CustomSchema(AutoSchema):
    title = 'Meu vendedor'
    description = 'Esse é a rota de venda'


# Seller

class SellerViewSet(ModelViewSet):
    """APIView subclass with custom schema introspection."""
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


# Client

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


# Product

class ProductViewSet(ModelViewSet):
    schema = None
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerDetail


# Sale

class SaleDetailViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
