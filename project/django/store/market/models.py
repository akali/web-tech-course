from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=256)


class Item(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    price = models.IntegerField()
    post_date = models.DateTimeField(auto_now=True)

    likes_count = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')

    def as_dict(self):
        return {
            'title': self.title
        }


class Like(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    def as_dict(self):
        return {
            'item': self.item.as_dict(),
            'author': self.author.id
        }


class Comment(models.Model):
    description = models.CharField(max_length=300)
    post_date = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='childs')
