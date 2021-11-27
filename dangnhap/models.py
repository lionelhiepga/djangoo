from django.db import models

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=45, null=False)
    email = models.EmailField()
    password = models.CharField(max_length= 50, null = False)
    
    def __str__(self):
        return str(self.email)
