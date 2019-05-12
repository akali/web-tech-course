from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers
from .models import Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)

# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(required=True)
#     body = serializers.CharField(required=True)
#     like_count = serializers.IntegerField()
#     created_at = serializers.DateTimeField()
#     created_by = UserSerializer(read_only=True)
#
#     def create(self, validated_data):
#         post = Post(**validated_data)
#         post.save()
#         return post
#
#     def update(self, instance, validated_data):
#         instance.body = validated_data.get('body', instance.body)
#         instance.save()
#         return instance
#
#
# class PostSerializer2(serializers.ModelSerializer):
#     title = serializers.CharField(required=True)
#     body = serializers.CharField(required=True)
#     like_count = serializers.IntegerField()
#     created_at = serializers.DateTimeField()
#     created_by = UserSerializer(read_only=True)
#
#     class Meta:
#         model = Post
#         fields = ('title', 'body', 'like_count', 'created_at', 'created_by')
#         # fields = '__all__'
#
#
