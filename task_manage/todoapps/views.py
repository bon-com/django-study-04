from django.shortcuts import render
from django.views.generic import ListView
from .models import Todo


class ListTaskView(ListView):
    """タスク一覧表示"""

    # テンプレート名称
    template_name = "todo/top.html"
    # モデル名称
    model = Todo
    # コンテキストの変数名
    context_object_name = "tasks"

    def get_queryset(self):
        """一覧取得メソッドのオーバーライド"""
        return Todo.objects.filter(status=0, user=self.request.user).order_by(
            "due_date"
        )
