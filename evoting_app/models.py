from django.db import models
import string
import random


class Voter(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def generate_token(self, length=6):
        """
        Generates a random token of specified length
        and saves it to the voter object.
        """
        letters_and_digits = string.ascii_letters + string.digits
        token = ''.join(random.choice(letters_and_digits) for i in range(length))
        self.token = token
        return token


class Candidate(models.Model):
    name = models.CharField(max_length=255)
    party = models.ForeignKey('Party', on_delete=models.CASCADE, related_name="candidates")

    def __str__(self):
        return self.name


class Party(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='party_symbols')
    description = models.TextField()

    def __str__(self):
        return self.name


class Vote(models.Model):
    voter = models.ForeignKey(Voter, null=True, on_delete=models.SET_NULL, related_name="votes")
    party = models.ForeignKey(Party, null=True, on_delete=models.SET_NULL, related_name="votes")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.voter.first_name} {self.voter.last_name} voted for {self.party.name} at {self.timestamp}"


class Result(models.Model):
    total_votes_cast = models.IntegerField()
    winning_party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name="results")
    number_of_vote_casted = models.CharField(max_length=100000)
    number_of_vote_for_each_party = models.CharField(max_length=1000000)

    def __str__(self):
        return f"{self.total_votes_cast} votes were cast, and the winning party is {self.winning_party.name}"


class Verification(models.Model):
    voter = models.ForeignKey(Voter, null=True, on_delete=models.CASCADE, related_name="verifications")
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.voter.first_name} {self.voter.last_name} was verified at {self.timestamp}, status: {self.status}"
