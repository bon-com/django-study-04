from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    """会員登録フォーム"""

    class Meta:
        model = User
        fields = ("username",)
