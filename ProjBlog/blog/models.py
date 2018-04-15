from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User,related_name="blog_posts")  # 允许通过类User反向查找到BlogArticles
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)  # 以倒序显示

    def __str__(self):
        return  self.title

class T1e(models.Model):
    auttitle = models.CharField(max_length=300)
    aut = models.ForeignKey(User, related_name="blog_post1s")

    class Meta:
        verbose_name = 'Test123'