from django.db import models
from . import Favorite
from . import Used
from . import Puzzle


# Create your models here.
class Player(models.Model):
    """
    A player model
    Attributes:
        user: 1-to-1 correlation to a user in the system.
        solved_puzzles: an int containing number of solved puzzles
        solved_words: an int of number of solved words
        show_me: an int of number of helps
        puzzleId: a one-to-many to a puzzle config
        favoriteId: one-to-many to a word
        usedId: one-to-many to a word
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favoriteId = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    usedId = models.ForeignKey(Used, on_delete=models.CASCADE)
    puzzleId = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    solvedPuzzles = models.IntgerField(on_delete=models.CASCADE)
    solvedWords = models.IntgerField(on_delete=models.CASCADE)
    showMe =  models.IntgerField(on_delete=models.CASCADE)

    class Meta:
        """
        Class to set the plural of the model as 'Players'
        """
        verbose_name_plural = "Players"

    def __str__(self):
        """
        Method to render a given player as a string. Helpful for
        interactions.
        :return:
        A string of the player's username
        """
        return '{}'.format(self.user.username)
