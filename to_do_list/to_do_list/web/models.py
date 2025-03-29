from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=30)
    task_description = models.TextField(max_length=350)
    category = models.CharField(max_length=20)