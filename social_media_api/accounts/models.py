from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    followers = models.ManyToManyField('self',symmetrical=False,blank=True )

    # This is the new field to track who this user is following
    following = models.ManyToManyField('self', symmetrical=False, related_name='followed_by', blank=True)


    def __str__(self):
        return self.username
