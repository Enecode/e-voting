from rest_framework import serializers
from .models import Vote, Voter, Verification, Party, Candidate, Result


class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = [
            'status',
            'voters',
            'timestamp'
        ]
