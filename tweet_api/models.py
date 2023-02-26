from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TweetModel(models.Model):
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    content = models.TextField(blank=True,null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tweet"
        ordering = ['-dateCreated']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True,null=True)
    profilePicture = models.FileField(upload_to='images/',blank=True,null=True)