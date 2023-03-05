from django.db import models


class Voter(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Candidate(models.Model):
    name = models.CharField(max_length=255)
    party = models.ForeignKey('Party', on_delete=models.CASCADE, related_name="party")

    def __str__(self):
        return self.name


class Party(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='party_symbols')
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="candidate")
    description = models.TextField()

    def __str__(self):
        return self.name


class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.voter.first_name} {self.voter.last_name} with an {self.voter.voter_id} voted for {self.party.name} at {self.timestamp}"


class Result(models.Model):
    total_votes_cast = models.IntegerField()
    winning_party = models.ForeignKey(Party, on_delete=models.CASCADE)
    number_of_vote_casted = models.CharField(max_length=100000)
    number_of_vote_for_each_party = models.CharField(max_length=1000000)

    def __str__(self):
        return f"{self.total_votes_cast} votes were cast, and the winning party is {self.winning_party.name}"


class Verification(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.voter.first_name} {self.voter.last_name} was verified at {self.timestamp}, status: {self.status}"
