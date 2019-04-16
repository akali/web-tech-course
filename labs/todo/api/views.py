from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from api.models import TaskList, Task


def get_task_lists(request):
    result = TaskList.objects.all()
    result = [x.to_json() for x in result]
    return JsonResponse(result, safe=False)


def get_task_list(request, id):
    return JsonResponse(TaskList.objects.get(id=id).to_json())


def get_tasks_of_task_list(request, id):
    return JsonResponse([x.to_json() for x in TaskList.objects.get(id=id).task_set.all()], safe=False)


def get_task(request, id):
    return JsonResponse(Task.objects.get(id=id).full(), safe=False)
