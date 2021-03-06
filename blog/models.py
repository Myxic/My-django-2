from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField(default=200)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    Created_date = models.DateTimeField(auto_now=True)
    Published_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Title

    def __str__(self):
        return self.Title

