from django.db import models
from . import Player


# Create your models here.
class Used(models.Model):
    """
    A model for Used or unfavorited words
    Attributes:
        playerId: FK to player
        word: a word
    """

    playerId = models.ForeignKey(Player, on_delete=models.CASCADE)
    word = models.CharField(max_length=30)

    class Meta:
        """
        Class to set the plural of the model as 'Used'
        """
        verbose_name_plural = "used"

    def __str__(self):
        """
        Method to render a given player as a string. Helpful for
        interactions.
        :return:
        A string of the player's username
        """
        return '{}'.format(self.word)
