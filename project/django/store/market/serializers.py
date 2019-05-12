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
    post_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", required=False)
    category_id = serializers.IntegerField()

    class Meta:
        model = Item
        fields = ('id', 'title', 'description', 'price', 'post_date', 'category_id')

    def create(self, validated_data):
        print(validated_data)
        category_id = validated_data.pop('category_id')
        category = Category.objects.get(pk=category_id)
        item = Item.objects.create(category=category, **validated_data)
        return item


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


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    item = ItemSerializer()
    description = serializers.CharField(required=True)
    post_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", required=False)

    class Meta:
        model = Item
        fields = ('id', 'description', 'post_date',)
