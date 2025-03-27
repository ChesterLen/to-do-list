from rest_framework import serializers
from django.views import generic as views
from to_do_list.web import forms, models
from django.urls import reverse_lazy


class CreateTaskView(views.CreateView):
    form_class = forms.CreateTaskForm
    template_name = 'create_task.html'
    success_url = reverse_lazy('create_task')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = models.Task.objects.all()
        return context