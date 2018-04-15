from django.db import models

# Create your models here.
class Te(models.Model):
    auttitle = models.CharField(max_length=300)
    author = models.ForeignKey('BlogArticles', related_name="blog_posts")

class BlogArtic(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User,related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return  self.title

