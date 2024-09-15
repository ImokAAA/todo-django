from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    #Model for managing task entity in orm
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
