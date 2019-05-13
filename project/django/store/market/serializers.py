from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers
from .models import Category, Item, Like, Comment


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
    post_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", required=False)
    category_id = serializers.IntegerField()

    class Meta:
        model = Item
        fields = ('id', 'title', 'description', 'price', 'post_date', 'likes_count', 'category_id',)

    def create(self, validated_data):
        print(validated_data)
        category_id = validated_data.pop('category_id')
        category = Category.objects.get(pk=category_id)
        item = Item.objects.create(category=category, **validated_data)
        return item


class CommentSerializer(serializers.ModelSerializer):
    item_id = serializers.IntegerField()
    post_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", required=False)

    class Meta:
        model = Item
        fields = ('id', 'description', 'post_date', 'item_id')

    def create(self, validated_data):
        print(validated_data)
        item_id = validated_data.pop('item_id')
        item = Item.objects.get(pk=item_id)
        comment = Comment.objects.create(item=item, **validated_data)
        return comment


class LikeSerializer(serializers.ModelSerializer):
    item_id = serializers.IntegerField()

    class Meta:
        model = Like
        fields = ('id', 'item_id')

    def create(self, validated_data):
        print(validated_data)
        item_id = validated_data.pop('item_id')
        item = Item.objects.get(pk=item_id)
        item.likes_count += 1
        item.save()
        like = Like.objects.create(item=item, **validated_data)
        return like
