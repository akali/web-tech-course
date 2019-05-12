from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers
from .models import Category, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class LikeSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    author = UserSerializer()

    class Meta:
        model = Like
        fields = ('id',)
