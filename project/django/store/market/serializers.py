from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers
from .models import Category, Item, Like, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    id = serializers.IntegerField()

    def create(self, validated_data):
        category = Category(**validated_data)
        category.save()
        return category

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class CommentSerializer(serializers.Serializer):
    description = serializers.CharField()
    post_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", required=False)

    def create(self, validated_data):
        comment = Comment(**validated_data)
        comment.save()
        return comment

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class CommentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('description', 'post_date', 'author')


class ItemSerializer(serializers.ModelSerializer):
    post_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", required=False)
    category_id = serializers.IntegerField()

    class Meta:
        model = Item
        fields = ('id', 'title', 'description', 'price', 'post_date', 'likes_count', 'category_id')

    def create(self, validated_data):
        print(validated_data)
        category_id = validated_data.pop('category_id')
        category = Category.objects.get(pk=category_id)
        item = Item.objects.create(category=category, **validated_data)
        return item


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
