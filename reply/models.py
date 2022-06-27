from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from board.models import Post


class Reply(models.Model):
    contents=models.TextField()
    writer=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)

