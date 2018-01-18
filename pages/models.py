from django.db import models


class Sponsor(models.Model):
    company_name = models.CharField(max_length=100, null=True)
    promo = models.CharField(max_length=100, null=True)
    num_teams = models.IntegerField(null=True)

class Team(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    eventbrite_funds = models.FloatField(max_length=10, null=True, blank=True)
    corporate_funds = models.FloatField(max_length=10, null=True, blank=True)
    corporate_sponsor = models.ForeignKey(Sponsor, related_name='teams', blank=True, null=True)

    def __str__(self):
        return str(self.pk)

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    teammate = models.CharField(max_length=200, blank=True, null=True)
    team = models.ForeignKey(Team, related_name='players', blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Supporter(models.Model):
    supporter_name = models.CharField(max_length=100)
    player_name = models.CharField(max_length=100)
    player = models.ForeignKey(Player, related_name='supporters', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.supporter_name)
