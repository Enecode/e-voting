from django.shortcuts import render
from rest_framework import viewsets

from evoting_app.models import Verification
from evoting_app.serializers import VerificationSerializer


# Create your views here.
class VerificationViewSet(viewsets.ModelViewSet):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerializer
