from rest_framework import serializers
from .models import Vote, Voter, Verification, Party, Candidate, Result


class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = [
            'status',
            'voter',
            'timestamp'
        ]


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ['name', 'logo', 'candidate', 'description']


class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = ['first_name', 'last_name', 'phone_number', 'email']


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = ['total_votes_cast',
                  'winning_party',
                  'number_of_vote_casted',
                  'number_of_vote_for_each_party'
                  ]
