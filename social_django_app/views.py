from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from .models import *
from .serializers import *

# user creation

@api_view(['POST'])
@permission_classes([])
def create_user(request):
    user = User.objects.create(
        username = request.data['username'],
    )
    user.set_password(request.data['password'])
    user.save()
    
    profile = Profile.objects.create(
        user = user,
        first_name = request.data['first_name'],
        last_name = request.data['last_name'],
    )
    profile.save()
    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)

# profile CRUD

@api_view(['GET'])
def get_profile(request):
    user = request.user
    profile = user.profile
    serialized_profile = ProfileSerializer(profile)
    return Response(serialized_profile.data)

# user post CRUD

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_text_post(request):
    user = request.user

    post = TextPost.objects.create(
        user = user,
        post_text = request.data['text'],
        #time is handled automatically
        #"likes" starts out empty
    )
    post.save()
    
    post_serialized = TextPostSerializer(post)
    return Response(post_serialized.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_text_post(request):
    user = request.user
    id = request.data['id']
    post = TextPost.objects.get(pk=id)

    if post.user != user: #can only edit your own posts
        return Response(status=status.HTTP_400_BAD_REQUEST)

    post.post_text = request.data['text']
    post.save()
    
    post_serialized = TextPostSerializer(post)
    return Response(post_serialized.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_text_post(request):
    user = request.user
    id = request.data['id']
    post = TextPost.objects.get(pk=id)
    
    if post.user != user: #can only delete your own posts
        return Response(status=status.HTTP_400_BAD_REQUEST)

    post.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_posts(request):
    #grabs all posts and returns them
    user = request.user
    posts = TextPost.objects.all()
    posts_serialized = {}

    for post in posts:
        post_serialized = TextPostSerializer(post)
        posts_serialized[str(post_serialized.data["id"])] = post_serialized.data

    return Response(posts_serialized)