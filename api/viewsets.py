from rest_framework.viewsets import ModelViewSet

from app.models import *
from .serializers import *


class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SaleViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
