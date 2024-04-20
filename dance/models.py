from django.db import models
from django.conf import settings

class Dance(models.Model):   # pylint: disable=missing-class-docstring
    title = models.CharField(max_length=200)
    dance_info =models.TextField()   # pylint: disable=trailing-whitespace
    image_url = models.URLField(blank=True, null=True)   # pylint: disable=trailing-whitespace

    def __str__(self):
        return self.title + ""
        
class UserContent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images/')
    youtube_link = models.URLField(max_length=255)

    def __str__(self):
        return f"Content by {self.user.username}"