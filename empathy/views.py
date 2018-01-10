from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json 
from .models import LoginTable, StudentProfile
import mimetypes
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import os

from django.core.exceptions import ObjectDoesNotExist

# Create your views here. 

@csrf_exempt 
def validate(request):
    # Login Validation - 
    #     Checkes whether the received username and password are valid or not
    
    js = json.loads(request.body.decode('utf-8'))
    userName = js['Username'] 
    passWord = js['Password']
    # r

    print("Username : "+userName+"Password : " + passWord)
    try:
        dbObj = LoginTable.objects.filter(username = userName)
        print(dbObj)
        try:
            dbObj.get(password = str(passWord))
            # print(db.role)
            dic = {'message':'He he','name':'Abhijeet', 'roll_no':'CO15302', 'role':'faculty','gender':'male'}

            ls = [dic]
            responseText = str(ls)[1:-1]

        except ObjectDoesNotExist:
            responseText = 'Check either username or password is incorrect'

        return HttpResponse(responseText, content_type="text/plain")
    except:     
        return HttpResponse("No User Found", content_type="text/plain")

@csrf_exempt
def register(request):
    
    dbObj = StudentProfile()
    loginObj = LoginTable()
    js = json.loads(request.body.decode('utf-8'))

    try:
        StudentProfile.objects.get(roll_no = str(js["roll_no"]))
        print("Double Help")
        return HttpResponse("Record Exists", content_type="text/plain")

    except ObjectDoesNotExist:

        print(ObjectDoesNotExist)
        print("Hellp")
        dbObj.name = str(js["name"])
        dbObj.roll_no = str(js["roll_no"])
        dbObj.branch = str(js["branch"])
        dbObj.semester = str(js["semester"])
        dbObj.year = str(js["year"])
        dbObj.email = str(js["email"])
        dbObj.mobile = str(js["mobile"])
        djObj.role = str(js["role"])
        dbObj.save()

        loginObj.password =str(js["roll_no"])
        loginObj.username = str(js["roll_no"])
        loginObj.role = str(js["role"])
        loginObj.save()

        return HttpResponse("success", content_type= "text/plain")
        
# Here's How we are going to send the PDF.
def output_pdf(request):
    the_file = 'media\Monkey and banana problem.pdf'
    
    with open(the_file,"rb") as f:
        data = f.read()

    response = HttpResponse(data, content_type = mimetypes.guess_type(the_file)[0])
    response['Content-Disposition'] = "attachment;filename = 'Monkey and banana problem.pdf'"
    response['Content-Length'] = os.path.getsize(the_file)

    return response


def event_register(request):
    pass
    # Js Data : {"name":"abhijeet rastogi","roll_no", Event:["event1","event2, "event3", "event4", "event5"]}

