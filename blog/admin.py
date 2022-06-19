from django.contrib import admin
from .models import Post


Class Post(admin.ModelAdmin):
   List_display =[
    "title", "text", "author", "created_date", "published_date"
    ]
