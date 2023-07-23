from django.urls import path
from . import views

urlpatterns = [path("tasks/", views.ListTaskView.as_view(), name="top")]
