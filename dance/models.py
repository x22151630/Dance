from django.db import models

class Dance(models.Model):   # pylint: disable=missing-class-docstring
    title = models.CharField(max_length=200)
    dance_info =models.TextField()   # pylint: disable=trailing-whitespace
    image_url = models.URLField(blank=True, null=True)   # pylint: disable=trailing-whitespace

    def __str__(self):
        return self.title + ""