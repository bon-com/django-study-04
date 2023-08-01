from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import SignupForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect	


class SignupView(CreateView):
    """会員登録"""

    model = User
    form_class = SignupForm
    template_name = "registration/signup.html"

    def form_valid(self, form):	
        # 最初にユーザーを保存する。なぜなら、ログインするためのユーザーが必要だからです。
        user = form.save()	
        # これは手動でユーザーをログインさせる方法です。
        login(self.request, user)	
        # これは特定のページにリダイレクトする方法です。
        return HttpResponseRedirect(reverse_lazy("top")) 
