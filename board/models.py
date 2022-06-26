from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    contents=models.TextField()
    creat_date=models.DateTimeField(auto_now_add=True)
    writer=models.ForeignKey(User, on_delete=models.CASCADE)