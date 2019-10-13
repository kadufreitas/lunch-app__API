from django.urls import path
from .views import view_client

urlpatterns = [
    path('clients/', view_client),
]