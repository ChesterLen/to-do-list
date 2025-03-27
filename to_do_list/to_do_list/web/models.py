from django.db import models

class Task(models.Model):
    IMPORTANT = 'Important'
    NOT_IMPORTANT = 'Not important'

    CHOICES = {
        IMPORTANT: 'Important',
        NOT_IMPORTANT: 'not important',
    }

    task_name = models.CharField(max_length=30)
    task_description = models.TextField(max_length=350)
    category = models.CharField(max_length=20, choices=CHOICES, default=NOT_IMPORTANT)