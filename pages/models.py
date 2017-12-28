from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    eventbrite_funds = models.FloatField(max_length=10, null=True, blank=True)
    corporate_funds = models.FloatField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.pk)

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200, unique=True)
    teammate = models.CharField(max_length=200, blank=True, null=True)
    team = models.ForeignKey(Team, related_name='players', blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
