from django.db import models
from django.contrib.auth.models import User


class TodoCategory(models.Model):
    """TODOカテゴリテーブル"""

    category_name = models.CharField("カテゴリ名", max_length=255, null=False)

    class Meta:
        verbose_name = "TODOカテゴリ"
        verbose_name_plural = "TODOカテゴリ"  # 左記を定義しないと、管理画面トップのテーブル名にsがついてしまう

    def __str__(self):
        # 下記を定義しないと、作成した内容が「TodoCategory object (1)」といったかたちで管理画面に表示される
        return self.category_name


class Todo(models.Model):
    """TODOタスクテーブル"""

    STATUS_CHOICES = [
        (0, "未完了"),
        (1, "完了"),
    ]

    task = models.CharField("タスク", max_length=255, null=False)
    memo = models.TextField("メモ", null=True, blank=True)
    status = models.IntegerField("ステータス", choices=STATUS_CHOICES, null=False)
    due_date = models.DateTimeField("期日", null=False)
    category = models.ForeignKey(
        TodoCategory, verbose_name="カテゴリID", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, verbose_name="利用者ID", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "TODOタスク"
        verbose_name_plural = "TODOタスク"  # 左記を定義しないと、管理画面トップのテーブル名にsがついてしまう

    def __str__(self):
        return self.task
