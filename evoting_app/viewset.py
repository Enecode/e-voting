from django.shortcuts import render
from rest_framework import viewsets
from .models import Verification, Party, Voter, Result
from .serializers import VerificationSerializer, PartySerializer, VoterSerializer, ResultSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import Verification


class VerificationViewSet(viewsets.ModelViewSet):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if Verification.objects.filter(voter__email=email, status=False).exists():
            return Response({'detail': 'A verification email has already been sent to this email.'}, status=400)
        voter = Voter.objects.get(email=email)
        verification = Verification.objects.create(voter=voter)
        token = str(verification.id)
        send_mail(
            'Verification Token',
            f'Your verification token is: {token}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return Response({'detail': 'Verification email sent.'}, status=201)

    def update(self, request, *args, **kwargs):
        token = request.data.get('token')
        verification = Verification.objects.filter(id=token, status=False).first()
        if verification:
            verification.status = True
            verification.save()
            return Response({'detail': 'Verification successful.'}, status=200)
        return Response({'detail': 'Invalid or expired token.'}, status=400)


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class VoterViewSet(viewsets.ModelViewSet):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
