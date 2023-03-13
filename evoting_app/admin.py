from django.contrib import admin
from .models import Voter, Candidate, Party, Vote, Result, Verification


class VoterAdmin(admin.ModelAdmin):
    list = ('first_Name', 'Last_name', 'phone_number', 'email')

    admin.site.register(Voter)

class CandidateAdmin(admin.ModelAdmin):
    list = ('name', 'party')

    admin.site.register(Candidate)


class PartyAdmin(admin.ModelAdmin):
    list = ('name', 'logo', 'candidate', 'description')

    admin.site.register(Party)


class VoteAdmin(admin.ModelAdmin):
    list = ('voter', 'party', 'timestamp', 'description')

    admin.site.register(Vote)


class ResultAdmin(admin.ModelAdmin):
    list = ('total_votes_cast', 'winning_part', 'number_of_vote_casted', 'number_of_vote_for_each_party')

    admin.site.register(Result)


class VerificationAdmin(admin.ModelAdmin):
    list = ('voter', 'status', 'timestamp')

    admin.site.register(Verification)