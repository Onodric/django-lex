from django.db import models


# Create your models here.
class player(models.Model):
    """
    A player model
    Attributes:
        user: 1-to-1 correlation to a user in the system.
        word: many-to-many to a word
        puzzle: a one-to-many to a dictionary
        solved_puzzles: an int containing number of solved puzzles
        solved_words: 
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)


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
