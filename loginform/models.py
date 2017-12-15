from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 200, primary_key = True)
    password = models.CharField(max_length = 100)
    name = models.CharField(max_length = 200)
    roll_no = models.CharField(max_length = 200)
    pic = models.ImageField(u"initial_picture")

    def __str__(self):
        return self.username

    
