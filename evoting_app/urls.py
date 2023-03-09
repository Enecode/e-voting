from django.urls import path, include
from rest_framework import routers

from .viewset import VerificationViewSet, PartyViewSet, VoterViewSet, ResultViewSet

app_name = 'evoting_app'
router = routers.DefaultRouter()
router.register(r'verification', VerificationViewSet)
router.register(r'party', PartyViewSet)
router.register(r'voter', VoterViewSet)
router.register(r'result', ResultViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
