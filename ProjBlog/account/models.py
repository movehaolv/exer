from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,unique=True,verbose_name='用户名')
    birth = models.DateField(blank=True,null=True,verbose_name='出生日期')
    phone = models.CharField(max_length=20,null=True,verbose_name='电话号码')

    # def __str__(self):
    #     return 'user {}'.format(self.user.username)

class Test(models.Model):
    ip = models.CharField(max_length=10)
    add= models.CharField(max_length=10)
