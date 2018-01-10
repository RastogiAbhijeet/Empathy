from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username = models.CharField(max_length = 200, primary_key = True)
    password = models.CharField(max_length = 100)
    role = role = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class StudentProfile(models.Model):
    roll_no = models.CharField(max_length = 10, primary_key = True)
    name = models.CharField(max_length = 100)
    branch = models.CharField(max_length = 5)
    semester = models.CharField(max_length = 4)
    year = models.CharField(max_length = 5)
    role = models.CharField(max_length=10, null=True, blank = True, default="None")
    email = models.CharField(max_length= 40, blank=True, null=True)
    mobile = models.CharField(max_length = 10, blank=True, null=True)
    event = models.CharField(max_length = 30, blank=True, null=True)
    position = models.IntegerField(blank = True, null=True)
    attribute_event = models.CharField(max_length = 30, blank = True, null=True)

    def __str__(self):
        return self.roll_no
        
# Select * where event = "xyz" from StudentProfile -- This is the filter for Faculty Searching events


    
    
