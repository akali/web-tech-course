from django.urls import path

from .views import views

urlpatterns = [
    path('', views.welcome_page),
    path('category', views.category),
    path('category/<int:pk>', views.category_items),
    path('item', views.item),
    path('item/<int:pk>', views.item_detail),
    path('like', views.like),
    path('comment', views.comment),
]




