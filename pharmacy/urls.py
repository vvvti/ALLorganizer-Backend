from django.urls import path
from .api import MedicineDoseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/medicine-dose', MedicineDoseViewSet, 'medicinedoses'),

urlpatterns = router.urls
