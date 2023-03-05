from django.db import models

# Create your models here.

class Team(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=150, blank=True, null=True)
    twitter_link = models.URLField(max_length=150, blank=True, null=True)
    google_plus_link = models.URLField(max_length=150, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName