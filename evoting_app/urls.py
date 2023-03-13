from django.urls import path, include
from rest_framework import routers
from .models import Voter, Party, Vote
from .viewset import VerificationViewSet, PartyViewSet, VoterViewSet, ResultViewSet, CandidateViewSet, VoteViewSet, \
    send_token_email, validate_token

app_name = 'evoting_app'
router = routers.DefaultRouter()
router.register(r'verification', VerificationViewSet)
router.register(r'party', PartyViewSet)
router.register(r'voter', VoterViewSet)
router.register(r'result', ResultViewSet)
router.register(r'candidate', CandidateViewSet)
router.register(r'vote', VoteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('send-token-email/', send_token_email, name='send_token_email'),
    path('validate-token/', validate_token, name='validate_token'),
    path('party/', Party, name="party"),
    path('voting/', Vote, name="vote"),
]

urlpatterns += router.urls
