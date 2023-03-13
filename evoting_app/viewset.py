import secrets

from django.template.defaulttags import csrf_token
from rest_framework.generics import get_object_or_404

from .models import Verification, Party, Voter, Result, Candidate, Vote
from .serializers import VerificationSerializer, PartySerializer, VoterSerializer, ResultSerializer, \
    CandidateSerializer, VoteSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

User = get_user_model()


@csrf_exempt
def send_token_email(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        voter = get_object_or_404(Voter, email=email)

        # Generate and save token to the voter object
        token = voter.generate_token()
        voter.save()

        # Send email with the token
        subject = 'Your registration token'
        message = f'Your registration token is {token}.'
        from_email = 'admin@example.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return JsonResponse({'success': True})

    return JsonResponse({'error': 'Invalid request method'})


@csrf_exempt
def validate_token(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        token = request.POST.get('token', None)
        voter = get_object_or_404(Voter, email=email, token=token)

        # Clear the token on successful validation
        voter.token = None
        voter.save()

        serializer = VoterSerializer(voter)

        return JsonResponse({'success': True, 'data': serializer.data})

    return JsonResponse({'error': 'Invalid request method'})


class VoterViewSet(viewsets.ModelViewSet):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer

    def create(self, request, *args, **kwargs):
        serializer = VoterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            voter = serializer.save()
            token = secrets.token_urlsafe()
            message = f"Your token is {token}."
            send_mail('Token', message, settings.EMAIL_HOST_USER, [voter.email], fail_silently=False)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
