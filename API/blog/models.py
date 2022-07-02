from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    text = models.TextField()


class Image(models.Model):
    alt_text = models.CharField(max_length=30)
    image = models.ImageField()
    article = models.ForeignKey(Article, null=False, on_delete=models.CASCADE)