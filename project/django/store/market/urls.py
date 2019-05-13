from django.urls import path

from .views import views, cbv_item, auth, cbv_category, cbv_comment, cbv_like

urlpatterns = [
    path('', views.welcome_page),
    path('login/', auth.login),
    path('logout/', auth.logout),
    path('category', cbv_category.CategoriesApi.as_view(), name='category'),
    path('category/<int:pk>', cbv_category.CategoryApi.as_view()),
    path('item', cbv_item.ItemApiView.as_view()),
    path('item/<int:pk>', cbv_item.ItemWithIdApiView.as_view()),
    path('like', cbv_like.LikeApiView.as_view()),
    path('comment', cbv_comment.CommentApiView.as_view()),
]




