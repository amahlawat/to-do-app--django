from django.db import models

# Create your models here.

class TodoListItem2(models.Model):
    description = models.TextField()
    status = models.TextField()

