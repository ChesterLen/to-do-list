from django.urls import path
from to_do_list.web import views


urlpatterns = [
    path('', views.CreateTaskView.as_view(), name='create_task'),
]