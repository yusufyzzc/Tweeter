from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    nickname = models.CharField(max_length=50)
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"Tweetnick: {self.nickname} message: {self.content[:50]}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweet_likes")
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="likes_set")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "tweet"], name="unique_user_tweet_like")
        ]

    def __str__(self):
        return f"{self.user.username} liked {self.tweet.id}"
