from django.db import models


class Dance(models.Model):   
    title = models.CharField(max_length=200)
    dance_info =models.TextField()   
    image_url = models.URLField(blank=True, null=True)   
    
    def __str__(self):
        return self.title + ""
