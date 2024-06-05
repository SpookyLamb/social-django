from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__" #["id", "username", "password"]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class TextPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextPost
        fields = ["id", "user", "post_text", "image", "created_at", "likes"]

