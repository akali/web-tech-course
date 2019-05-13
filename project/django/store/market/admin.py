from django.contrib import admin

from market.models import Category, Item, Like

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Like)
