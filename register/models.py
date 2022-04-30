from django.db import models

# Create your models here.
class register(models.Model):
    name = models.CharField(max_length=50)
    nickname= models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nickname + " (" + self.email + ")"
