from django.contrib import admin
from .models import Todo
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'created_at',
                    'updated_at', 'is_active')
    search_fields = ('task',)


admin.site.register(Todo, TaskAdmin)
