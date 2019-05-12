from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers
from .models import Category, Item, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class CategorySerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = ('id', 'title',)


class ItemSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    category = CategorySerializer()
    post_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", required=False)

    class Meta:
        model = Item
        fields = ('id', 'title', 'description', 'price', 'post_date',)


class LikeSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    author = UserSerializer()

    class Meta:
        model = Like
        fields = ('id',)


class LikeSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    author = UserSerializer()

    class Meta:
        model = Like
        fields = ('id',)


class LikeIdSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    author_id = serializers.IntegerField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
