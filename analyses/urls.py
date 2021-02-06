from django.urls import path
from .api import CrpAnalysisViewSet, CompleteBloodCountViewSet, ALT_ASTViewSet, UrineAnalisisViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/cbc', CompleteBloodCountViewSet, 'cbc'),
router.register('api/crp',
                CrpAnalysisViewSet, 'crp'),
router.register('api/alt_ast', ALT_ASTViewSet, 'alt_ast'),
router.register('api/urine',
                UrineAnalisisViewSet, 'urine'),

urlpatterns = router.urls
