from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^task_list_create_API_view/', views.TaskListCreateAPIView.as_view(), name='TaskListCreateAPIView'),
    url(r'^task_API_view/', views.TaskAPIView.as_view(), name='TaskAPIView'),
    url(r'^task_decorator/', views.TaskDecorator, name='TaskDecorator'),
]