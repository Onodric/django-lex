from django.db import models
from . import Favorite
from . import Used
from . import Puzzle


# Create your models here.
class Puzzle(models.Model):
    """
    A puzzle model
    Attributes:
        playerId: 1-to-1 correlation to a user in the system.
    """

    playerId = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """
        Class to set the plural of the model as 'Players'
        """
        verbose_name_plural = "puzzles"

    def __str__(self):
        """
        Method to render a given player as a string. Helpful for
        interactions.
        :return:
        A string of the player's username
        """
        return 'most recent puzzle.'
