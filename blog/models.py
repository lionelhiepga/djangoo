from datetime import datetime
from django.db import models
from django.utils import timezone


class Postform(models.Model):
    title = models.CharField(max_length= 100, null= False)
    content = models.TextField()
    creat_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    # def was_published_recently(self):
        return self.creat_at >= timezone.now() - datetime.timedelta(days = 1)
