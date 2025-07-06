from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    founded = models.IntegerField()
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    match_date = models.DateField()
    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"