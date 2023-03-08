from django.urls import path, include
from rest_framework import routers

from . import viewset
from .viewset import PartyViewSet, VoterViewSet, VerificationViewSet

app_name = 'evoting_app'
router = routers.DefaultRouter()
router.register(r'verifications', viewset.VerificationViewSet, 'verification')
router.register(r'party', viewset.PartyViewSet, 'party')
router.register(r'voter', viewset.VoterViewSet, 'voter')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/verifications/', VerificationViewSet.as_view({'post': 'create'}), name='verifications'),
]
