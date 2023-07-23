# Generated by Django 4.2.3 on 2023-07-23 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TodoCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category_name",
                    models.CharField(max_length=255, verbose_name="カテゴリ名"),
                ),
            ],
            options={
                "verbose_name": "TODOカテゴリ",
                "verbose_name_plural": "TODOカテゴリ",
            },
        ),
        migrations.CreateModel(
            name="Todo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("task", models.CharField(max_length=255, verbose_name="タスク")),
                ("memo", models.TextField(blank=True, null=True, verbose_name="メモ")),
                ("status", models.IntegerField(verbose_name="ステータス")),
                ("due_date", models.DateTimeField(verbose_name="期日")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="todoapps.todocategory",
                        verbose_name="カテゴリID",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="利用者ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "TODOタスク",
                "verbose_name_plural": "TODOタスク",
            },
        ),
    ]
