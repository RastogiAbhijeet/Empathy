from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 100)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class StudentProfile(models.Model):
    
    roll_no = models.CharField(max_length = 10, primary_key=True)
    name = models.CharField(max_length = 100, default = "xyz", blank=True, null = True)
    branch = models.CharField(max_length = 5, default = "xyz", blank=True, null = True)
    semester = models.CharField(max_length = 4, default = "xyz", blank=True, null = True)
    year = models.CharField(max_length = 5, default = "xyz", blank=True, null = True)
    role = models.CharField(max_length = 20, default = "xyz", blank=True, null = True)
    email = models.CharField(max_length= 40, default = "xyz", blank=True, null = True)
    mobile = models.CharField(max_length = 10, default = "xyz", blank=True, null = True)
    gender = models.CharField(max_length = 10, default = "xyz", blank=True, null = True)
    college = models.CharField(max_length = 10, default = "Default", blank=True, null = True)

   
    def __str__(self):
        return self.roll_no

class EventTable(models.Model):
    event = models.CharField(max_length = 10)
    roll_no = models.CharField(max_length = 10)
    position = models.CharField(max_length = 10, null = True, blank = True, default = "Not Played Yet")
    attribute = models.CharField(max_length = 40, null = True, blank = True)

class RollNo(models.Model):
    roll_no = models.CharField(max_length = 8, primary_key = True)
    name = models.CharField(max_length = 300)
        
# Select * where event = "xyz" from StudentProfile -- This is the filter for Faculty Searching events


    
    
