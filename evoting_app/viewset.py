from django.shortcuts import render
from rest_framework import viewsets
from .models import Verification, Party, Voter
from .serializers import VerificationSerializer, PartySerializer, VoterSerializer


# Create your views here.
class VerificationViewSet(viewsets.ModelViewSet):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerializer


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class VoterViewSet(viewsets.ModelViewSet):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer
