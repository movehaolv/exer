from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,unique=True)
    birth = models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=20,null=True)

    # def __str__(self):
    #     return 'user {}'.format(self.user.username)

class Test(models.Model):
    ip = models.CharField(max_length=10)
    add= models.CharField(max_length=10)