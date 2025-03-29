from rest_framework import serializers
from to_do_list.web import models
from rest_framework import generics as api_views
from django.views import generic as views

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'


class RestApiTaskView(api_views.ListAPIView):
    serializer_class = TaskSerializer
    queryset = models.Task.objects.all()


class HomePageView(views.TemplateView):
    template_name = 'home_page.html'