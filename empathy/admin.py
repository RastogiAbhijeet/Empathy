from django.contrib import admin
from .models import LoginTable, StudentProfile, EventTable,RollNo
# Register your models here.

class StudentTitle(admin.ModelAdmin):
    list_display = ('roll_no', "name")

class EventTitle(admin.ModelAdmin):
    list_display = ('event','roll_no', 'position')

class RollTitle(admin.ModelAdmin):
    list_display = ("roll_no", "name")

admin.site.register(LoginTable)
admin.site.register(StudentProfile, StudentTitle)
admin.site.register(EventTable, EventTitle)
admin.site.register(RollNo, RollTitle)

# CO16501
# ABHISHEK ZADE