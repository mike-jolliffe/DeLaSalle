from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    funding = models.FloatField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    team = models.ForeignKey(Team, related_name='players')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
