from django.shortcuts import render
from rest_framework import viewsets
from evoting_app.models import Verification, Party
from evoting_app.serializers import VerificationSerializer, PartySerializer


# Create your views here.
class VerificationViewSet(viewsets.ModelViewSet):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerializer


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer