from django.db import models

# Create your models here.


class Todo(models.Model):
    task = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # file_attachment = models.FileField()
    is_fileAttached = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_completed = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    is_deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
