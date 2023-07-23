from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from .forms import SignupForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class SignupView(CreateView):
    """会員登録"""

    model = User
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("top")

    def form_valid(self, form):
        """会員登録後にログインさせる"""
        # まず、親クラスのform_validを呼び出して、ユーザーを作成
        valid = super().form_valid(form)

        # ユーザーを認証
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")  # パスワードはcleaned_dataから取得
        user = authenticate(username=username, password=password)

        # ユーザーをログインさせる
        if user is not None:
            login(self.request, user)

        return valid
