from django.db import models

class TodoModel(models.Model):
    todo = models.CharField(max_length = 50)

    
