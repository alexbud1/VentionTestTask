from django.contrib import admin

from .models import (
    Category,
    Task,
)


class CategoryAdminView(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class TaskAdminView(admin.ModelAdmin):
    list_display = ('title', 'completed', 'category')
    list_filter = ['completed']
    search_fields = ('title', 'category__name')


admin.site.register(Category, CategoryAdminView)
admin.site.register(Task, TaskAdminView)
