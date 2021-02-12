from django.urls import path
from .api import ProtocolViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/protocol', ProtocolViewSet, 'protocols'),

urlpatterns = router.urls
