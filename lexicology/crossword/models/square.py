from django.db import models
from . import Puzzle


# Create your models here.
class Square(models.Model):
    """
    A square model -- there will be many of these per puzzle.
    Attributes:
        puzzleId: foreign key for the containing square
        index: an int containing number of solved puzzles
        x: an int for horizontal (column) coordinate
        y: an int for vertical (row) coordinate
        across_word: charfield containing a possible word. initialized to Null
        down_word: charfield containing a possible word. initialized to Null
        letter: the letter found in the square. initialized to Null

    """

    puzzleId = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    index = models.IntegerField(on_delete=models.CASCADE)
    x = models.IntegerField(on_delete=models.CASCADE)
    y = models.IntegerField(on_delete=models.CASCADE)
    across_word = models.CharField(max_length=30, on_delete=models.CASCADE)
    down_word = models.CharField(max_length=30, on_delete=models.CASCADE)
    letter = models.CharField(max_length=1, on_delete=models.CASCADE)

    class Meta:
        """
        Class to set the plural of the model as 'Players'
        """
        verbose_name_plural = "squares"

    def __str__(self):
        """
        Method to render a given player as a string. Helpful for
        interactions.
        :return:
        A string of the player's username
        """
        return '{0} at [{1}, {2}]: {3}'.format(self.index, self.x, self.y,
                                       self.letter)
