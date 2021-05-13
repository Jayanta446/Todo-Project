from django.contrib import admin
from .models import TodoModel

@admin.register(TodoModel)
class TodoAdmin(admin.ModelAdmin):
    list_display =['id','todo']


    
