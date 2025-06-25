from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tweet(models.Model):
    content = models.TextField(max_length=280)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_tweets', blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.author.username}: {self.content[:50]}..."
    
    def total_likes(self):
        return self.likes.count()
