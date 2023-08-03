from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from . import models
from django.views.generic.edit import CreateView, DeleteView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


class ListTaskView(LoginRequiredMixin, ListView):
    """タスク一覧表示"""

    # テンプレート名称
    template_name = "todo/top.html"
    # モデル名称
    model = models.Todo
    # コンテキスト変数名
    context_object_name = "tasks"
    # ページネーション（1ページあたりの項目数）
    paginate_by = 5

    def get_queryset(self):
        """一覧取得メソッドのオーバーライド"""
        return models.Todo.objects.filter(status=0, user=self.request.user).order_by(
            "due_date"
        )


class DetailTaskView(DetailView):
    """タスク詳細表示"""

    # テンプレート名称
    template_name = "todo/detail.html"
    # モデル名称
    model = models.Todo
    # コンテキスト変数名
    context_object_name = "todo"


class TodoCreateView(CreateView):
    """タスク新規登録画面"""

    model = models.Todo
    template_name = "todo/create.html"
    fields = ["task", "memo", "status", "due_date", "category"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("top")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["categories"] = models.TodoCategory.objects.all()
        return context


class DeleteTaskView(DeleteView):
    """タスクの削除"""

    template_name = "todo/todo_confirm_delete.html"
    model = models.Todo
    success_url = reverse_lazy("top")


class TodoEditView(UpdateView):
    """タスクの編集"""

    model = models.Todo
    fields = ["task", "memo", "due_date", "category", "status"]
    template_name = "todo/edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["categories"] = models.TodoCategory.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy("detail", kwargs={"pk": self.object.pk})


def todo_complete(request, tid):
    """ステータス完了"""
    todo = get_object_or_404(models.Todo, pk=tid)
    todo.status = 1
    todo.save()
    return HttpResponseRedirect(reverse_lazy("top"))
