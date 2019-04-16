from django.urls import path

from api.views import get_task_lists, get_task_list, get_tasks_of_task_list, get_task

urlpatterns = [
    path('task_lists', get_task_lists),
    path('task_lists/<int:id>', get_task_list),
    path('task_lists/<int:id>/tasks/', get_tasks_of_task_list),
    path('task_lists/<int:id>', get_task),
]
