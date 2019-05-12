from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers
from .models import Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class CategorySerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)

    def create(self, validated_data):
        category = Category(**validated_data)
        category.save()
        return category

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance

    class Meta:
        model = Category
        fields = ('title')
        # fields = '__all__'
