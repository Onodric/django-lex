from django.db import models
from . import Player


# Create your models here.
class Favorite(models.Model):
    """
    A model for storing used words
    Attributes:
        playerId: FK to player
        word: a word
    """

    playerId = models.ForeignKey(Player, on_delete=models.CASCADE)
    word = models.CharField(max_length=30)

    class Meta:
        """
        Class to set the plural of the model as 'Players'
        """
        verbose_name_plural = "favorites"

    def __str__(self):
        """
        Method to render a given player as a string. Helpful for
        interactions.
        :return:
        A string of the player's username
        """
        return '{}'.format(self.word)
