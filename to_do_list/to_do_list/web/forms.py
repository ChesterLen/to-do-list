from django import forms
from to_do_list.web import models


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = '__all__'