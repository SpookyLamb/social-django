from django.db import models
from django.contrib.auth.models import User #users

class Profile (models.Model): #profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    email = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self) -> str:
        return self.user.username

class TextPost (models.Model): #text posts
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts") #user who made this post
    post_text = models.CharField(max_length=280) #actual post text content
    created_at = models.DateTimeField(auto_now_add=True) #tracks the date the post was made
    likes = models.ManyToManyField(User) #tracks the users that have liked this post
    image = models.ImageField(upload_to='images/', null=True, default=None) #contains an image URL, defaults to None if a value is not provided

    def __str__(self) -> str:
        return self.post_text
