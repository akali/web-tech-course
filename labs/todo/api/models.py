from django.db import models


# Create your models here.

class TaskList(models.Model):
    name = models.CharField('name', max_length=200)

    def full(self):
        obj = {
            'id': self.id,
            'name': self.name,
        }
        return obj

    def to_json(self):
        return self.full()


class Task(models.Model):
    name = models.CharField('name', max_length=200)
    created_at = models.DateTimeField('created_at', auto_now=True)
    due_on = models.DateTimeField('due_on', auto_now=True)
    status = models.CharField('status', default='TODO', max_length=200)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def full(self):
        obj = {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status
        }
        return obj

    def to_json(self):
        obj = {
            'id': self.id,
            'name': self.name,
        }
        return obj
