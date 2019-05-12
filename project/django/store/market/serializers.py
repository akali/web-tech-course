from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers
from .models import Category, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class LikeSerializer(serializers.ModelSerializer):
    item = serializers.ItemSerializer(read_only=True)
    author = serializers.UserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ('author', 'item', )
