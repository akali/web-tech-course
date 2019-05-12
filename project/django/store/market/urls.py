from django.urls import path

from .views import views, cbv_item, auth

urlpatterns = [
    path('/', views.welcome_page),
    path('login/', auth.login),
    path('logout/', auth.logout),
    path('category', views.category),
    path('category/<int:pk>', views.category_items),
    path('item', cbv_item.ItemApiView.as_view()),
    path('item/<int:pk>', cbv_item.ItemWithIdApiView.as_view()),
    path('like', views.like),
    path('comment', views.comment),
]




