from django.urls import path, include
from rest_framework import routers

from .views import VerificationViewSet, PartyViewSet

app_name = 'evoting_app'
router = routers.DefaultRouter()
router.register(r'verification', VerificationViewSet)
router.register(r'party', PartyViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
