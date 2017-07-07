from django.db import models


# Create your models here.
class player(models.Model):
    """
    A player model with 1-to-1 correlation to a user in the system. To be
    fleshed out
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        """

        """
        verbose_name_plural = "Players"

    def __str__(self):
        """

        :return:
        """
        return '{}'.format(self.user.username)
