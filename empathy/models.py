from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username = models.CharField(max_length = 200, primary_key = True)
    password = models.CharField(max_length = 100)

    def __str__(self):
        return self.username

# class NewsFeed(models.Model):
#     ngo_name = models.CharField(max_length = 300)
#     title = models.CharField(max_length = 300)
#     date = models.DateField()
#     Description = models.CharF