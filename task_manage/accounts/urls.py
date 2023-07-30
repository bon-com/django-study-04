from django.urls import path, include
from . import views
from django.contrib import auth

urlpatterns = [
    # path("", include("django.contrib.auth.urls")),
    path("login/", auth.views.LoginView.as_view(), name="login"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("logout/", auth.views.LogoutView.as_view(), name="logout"),
]
