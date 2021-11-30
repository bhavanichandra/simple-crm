from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LeadView, AddressViewSet

router = DefaultRouter()
router.register('leads', LeadView, 'leads')
router.register('address', AddressViewSet, 'address')

urlpatterns = [
    path('', include(router.urls)),
]
