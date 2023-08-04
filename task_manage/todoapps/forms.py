from django import forms
from . import models
from task_manage import consts


class TodoFormBase(forms.ModelForm):
    """Todoテーブル共通フォーム"""

    # タスク必須チェックメッセージ変更
    task = forms.CharField(
        error_messages={
            consts.INPUT_REQUIRED: "タスク名は必須です。"
        }
    )
    # 期日必須チェックメッセージ変更
    due_date = forms.DateTimeField(
        error_messages={
            consts.INPUT_REQUIRED: "タスク期日は必須です。"
        }
    )
    # カテゴリ必須チェックメッセージ変更
    # ForeignKeyのエラーメッセージをカスタマイズする場合、
    # フィールドを再定義する必要あり
    category = forms.ModelChoiceField(
        # 選択肢として表示するデータリストを設定
        queryset = models.TodoCategory.objects.all(),
        error_messages={
            consts.INPUT_REQUIRED: "カテゴリは必須です。"
        }
    )
    # ステータス必須チェックメッセージ変更
    status = forms.IntegerField(
        error_messages={
            consts.INPUT_REQUIRED: "ステータスは必須です。"
        }
    )

    class Meta:
        # フィールドと入力チェックの自動生成用
        model = models.Todo
        # 画面表示項目
        fields = ["task", "memo", "due_date", "category"]


class TodoEditForm(TodoFormBase):
    """タスク編集用フォーム"""

    class Meta(TodoFormBase.Meta):
        # 画面表示項目
        fields = ["task", "memo", "due_date", "category", "status"]
