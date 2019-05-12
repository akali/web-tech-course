from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers
from .models import Category, Item


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class CategorySerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = ('title')


class ItemSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    category = CategorySerializer()
    post_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", required=False)

    class Meta:
        model = Item
        fields = ('id', 'title', 'description', 'price', 'post_date',)
