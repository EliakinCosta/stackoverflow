from django.db import models


class characterTable(models.Model):
    userID = models.CharField(max_length = 32)
    playerName = models.CharField(max_length = 32)
    race = models.CharField(max_length = 32)
    playerClass = models.CharField(max_length = 32)
    strength = models.CharField(max_length = 2)
    dexterity = models.CharField(max_length = 2)
    constitution = models.CharField(max_length = 2)
    intelligence = models.CharField(max_length = 2)
    wisdom = models.CharField(max_length = 2)
    charisma = models.CharField(max_length = 2)

    def __str__(self):
        return (self.userID + ": " + self.playerName )
