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
    post_text = models.TextField() #actual post text content
    created_at = models.DateTimeField(auto_now_add=True) #tracks the date the post was made
    likes = models.ManyToManyField(User) #tracks the users that have liked this post

    def __str__(self) -> str:
        return self.post_text

class ImagePost (TextPost): #image posts, extends text posts
    image = models.ImageField(upload_to='images/') #contains an image URL

    def __str__(self) -> str:
        return self.post_text
