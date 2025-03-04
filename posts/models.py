from django.db import models

# Create your models here.
class Post(models.Model):
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Response(models.Model):
    question = models.ForeignKey(Post, on_delete=models.CASCADE)
    response_text = models.CharField(max_length=200)