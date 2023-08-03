from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from task_manage import consts


class SignupForm(UserCreationForm):
    """会員登録フォーム"""

    # 独自入力チェック定義-------------
    # ユーザー名
    username = forms.CharField(
        max_length=100,
        error_messages={
            consts.INPUT_REQUIRED: "ユーザー名は必須です。",
            consts.INPUT_MAX_LENGTH: "ユーザー名は最大100文字までです"
        }
    )
    # パスワード
    password1 = forms.CharField(
        validators=[MinLengthValidator(8, message="パスワードは最低8文字以上必要です。")],
        error_messages={
            consts.INPUT_REQUIRED: "パスワードは必須です。"
        }
    )
    # パスワード確認用
    password2 = forms.CharField(
        validators=[MinLengthValidator(8, message="パスワード（確認用）は最低8文字以上必要です。")],
        error_messages={
            consts.INPUT_REQUIRED: "パスワード（確認用）は必須です。"
        }
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")