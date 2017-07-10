from django.db import models
from . import Favorite
from . import Used
from . import Puzzle


# Create your models here.
class Clue(models.Model):
    """
    A model for holding a puzzle clue
    Attributes:
        puzzleId: a one-to-many to a puzzle config
        word: an int containing number of solved puzzles
        definition: an int of number of solved words
    """

    puzzleId = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    word = models.CharField(max_length=30, on_delete=models.CASCADE)
    definition = models.TextField(on_delete=models.CASCADE)

    class Meta:
        """
        Class to set the plural of the model as 'clues'
        """
        verbose_name_plural = "clues"

    def __str__(self):
        """
        Method to render a given clue as a string. Helpful for
        interactions.
        :return:
        A string of the player's username
        """
        return '{0}: {1}'.format(self.word, self.definition)
