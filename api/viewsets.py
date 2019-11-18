from rest_framework.viewsets import ModelViewSet

from app.models import Seller, Client, Product, Sale
from .serializers import (
    SellerSerializer,
    ClientSerializer,
    ProductSerializer,
    ProductSerializerDetail,
    SaleSerializer,
)


# Seller

class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


# Client

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


# Product

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerDetail


# Sale

class SaleDetailViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
