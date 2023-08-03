from django import forms
from . import models


class TodoForm(forms.ModelForm):
    """Todoテーブル共通フォーム"""

    class Meta:
        # フィールドと入力チェックの自動生成用
        model = models.Todo
        # 画面表示項目
        fields = ["task", "memo", "due_date", "category", "status"]
