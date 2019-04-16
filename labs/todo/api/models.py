from django.db import models


# Create your models here.

class TaskList(models.Model):
    name = models.CharField('name', max_length=200)


class Task(models.Model):
    name = models.CharField('name', max_length=200)
    created_at = models.DateTimeField('created_at', auto_now=True)
    due_on = models.DateTimeField('due_on', auto_now=True)
    status = models.CharField('status', default='TODO')
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
