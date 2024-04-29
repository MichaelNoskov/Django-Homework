from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from datetime import date
from django.utils.translation import gettext_lazy as _

from .models import Task, Developer, Comment, TaskDeveloper


class TaskDeveloperInline(admin.TabularInline):
    model = TaskDeveloper
    extra = 1


@admin.register(Task)
class ClientAdmin(admin.ModelAdmin):
    model = Task
    inlines = (TaskDeveloperInline,)


@admin.register(Developer)
class AuthorAdmin(admin.ModelAdmin):
    model = Developer
    inlines = (TaskDeveloperInline,)


@admin.register(Comment)
class GenreAdmin(admin.ModelAdmin):
    model = Comment
