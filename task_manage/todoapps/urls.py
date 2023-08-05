from django.views.generic.base import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.RedirectTopView.as_view(), name="home"),
    path("tasks/", views.ListTaskView.as_view(), name="top"),
    path("tasks/detail/<int:pk>", views.DetailTaskView.as_view(), name="detail"),
    path("tasks/create/", views.TodoCreateView.as_view(), name="create_task"),
    path("task/delete/<int:pk>", views.DeleteTaskView.as_view(), name="delete_task"),
    path("task/edit/<int:pk>", views.TodoEditView.as_view(), name="edit_task"),
    path("task/complete/<int:tid>", views.todo_complete, name="complete_task"),
    path("taks/error", views.ErrorView.as_view(), name="error"),
]
