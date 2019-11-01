from django.urls import include, path
from rest_framework import routers
from .viewsets import *

router = routers.DefaultRouter()
router.register(r'sellers', SellerViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'products', ProductViewSet)
router.register(r'products-detail', ProductListViewSet)
router.register(r'sales', SaleDetailViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]