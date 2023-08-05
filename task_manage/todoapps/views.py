from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, RedirectView
from . import models
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from task_manage import consts


class RedirectTopView(RedirectView):
    """タスク一覧画面にリダイレクト"""

    url = reverse_lazy("top")

class ListTaskView(LoginRequiredMixin, ListView):
    """タスク一覧表示"""

    # DB参照モデル
    model = models.Todo
    # テンプレート
    template_name = "todo/top.html"
    # コンテキスト変数の修正
    context_object_name = "tasks"
    # ページネーション（1ページあたりの項目数）
    paginate_by = 5

    def get_queryset(self):
        """一覧取得メソッドをオーバーライドする"""
        return models.Todo.objects.filter(status=0, user=self.request.user).order_by(
            "due_date"
        )


class DetailTaskView(LoginRequiredMixin, DetailView):
    """タスク詳細表示"""

    # DB参照モデル
    model = models.Todo
    # テンプレート
    template_name = "todo/detail.html"
    # コンテキスト変数の修正
    context_object_name = "todo"


class TodoCreateView(LoginRequiredMixin, CreateView):
    """タスク新規登録画面"""

    # DB登録対象
    model = models.Todo
    # テンプレート
    template_name = "todo/create.html"
    # 使用フォームクラス
    form_class = forms.TodoFormBase
    # 登録完了後のURL
    success_url = reverse_lazy("top")

    def get_context_data(self, **kwargs):
        """コンテキストをオーバーライドする"""
        # 既存コンテキスト取得
        context = super().get_context_data(**kwargs)
        # カテゴリ一覧を追加
        context["categories"] = models.TodoCategory.objects.all()
        return context

    def form_valid(self, form):
        """フォームバリデーション後の処理"""
        # フォームから生成されるモデルにユーザー追加
        form.instance.user = self.request.user
        # ステータスはデフォルトで0（未完了）とする
        form.instance.status = consts.TASK_STATUS_IMCOMPLETE
        # 親クラスのDB登録処理呼び出し
        return super().form_valid(form)


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    """タスクの削除"""

    # DB更新対象
    model = models.Todo
    # テンプレート
    template_name = "todo/todo_confirm_delete.html"
    # 更新成功後のURL
    success_url = reverse_lazy("top")


class TodoEditView(LoginRequiredMixin, UpdateView):
    """タスクの編集"""

    # DB登録対象
    model = models.Todo
    # テンプレート
    template_name = "todo/edit.html"
    # 使用フォームクラス
    form_class = forms.TodoEditForm

    def get_context_data(self, **kwargs):
        """コンテキストをオーバーライドする"""
        # 既存コンテキスト取得
        context = super().get_context_data(**kwargs)
        # カテゴリ一覧を追加
        context["categories"] = models.TodoCategory.objects.all()
        return context

    def get_success_url(self):
        """登録完了成功後のURLを返却する処理"""
        return reverse_lazy("detail", kwargs={"pk": self.object.pk})


def todo_complete(request, tid):
    """タスクのステータスを完了にする"""
    # タスク情報取得
    todo = get_object_or_404(models.Todo, pk=tid)
    # ステータスを1（完了）に更新
    todo.status = consts.TASK_STATUS_COMPLETE
    todo.save()
    # 一覧画面にリダイレクト
    return HttpResponseRedirect(reverse_lazy("top"))
