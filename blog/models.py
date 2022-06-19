from django.db import models


class Post(models.model):
   class Meta:
     verbose_name = "Post"
     verbose_name_plural = "Post"
   Title = models.CharField(max_length=200)
   Text = models.TextField(max_length=None)
   Author = models.get_user_model
   Created_Date = models.DateTimeField
   Published_Date = models.DateTimeField
    
