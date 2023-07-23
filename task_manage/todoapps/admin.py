from django.contrib import admin
from .models import Todo, TodoCategory

admin.site.register(Todo)
admin.site.register(TodoCategory)
