from django.urls import path
from to_do_list.web import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('task/api/view/', views.RestApiTaskView.as_view(), name='task_api_view'),
]