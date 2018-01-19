from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json 
from .models import LoginTable, StudentProfile, EventTable
import mimetypes
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import os

from django.core.exceptions import ObjectDoesNotExist

from django.core.mail import EmailMessage

# Create your views here. 

@csrf_exempt 
def validate(request):
    # Login Validation - 
    #     Checkes whether the received username and password are valid or not
    # responseText = ""
    js = json.loads(request.body.decode('utf-8'))
    userName = js['Username'] 
    passWord = js['Password']
    # r

    print("Username : "+userName+"Password : " + passWord)
    try:
        dbObj = LoginTable.objects.filter(username = userName)
        print(dbObj)
        try:
            dic = {}
            dbObj.get(password = str(passWord))
            for i in dbObj:
                print(i.role)

                if str(i.role) == "student":
                    studentObj = StudentProfile.objects.get(roll_no = passWord)
                    dic = {'name':studentObj.name, 'roll_no':studentObj.roll_no, 'role':studentObj.role,'gender':studentObj.gender,'branch':studentObj.branch,'CCET':studentObj.college}
                else:
                    dic = {'role':str(i.role)}
            print(dic)
            ls = [dic]
            responseText = str(ls)[1:-1]

        except ObjectDoesNotExist:
            responseText = 'Check either username or password is incorrect'
            # return HttpResponse(responseText, content_type="text/plain")
        except Exception as e:
            print(e)

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
        dbObj.role = str(js["role"])
        dbObj.gender = str(js["gender"])
        dbObj.college = str(js["college"])
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

@csrf_exempt
def event_register(request):
    
    try:
        # print("Hello")
        js = json.loads(request.body.decode("utf-8"))
        jsArray = js['event']
        print(jsArray);
        dbObj = EventTable.objects.filter(roll_no = str(js["roll_no"]))

        list_registered = []
        for x in dbObj:
            list_registered.append(x)
        
        if len(dbObj)+len(jsArray) > 5:
            response_str = "Already have registered for events"
            for i in dbObj:
                response_str = response_str + "   " +str(i.event)

            return HttpResponse(response_str, content_type="text/plain")
        else:
            
            for i in jsArray:
                if i not in list_registered:
                    db = EventTable()
                    print(i)
                    db.roll_no = js["roll_no"]
                    db.event = i
                    db.save()

            return HttpResponse("Check profile to see the registered Events", content_type="text/plain")

    except Exception as e:
        print(e)

    return HttpResponse("Try Again after some time", content_type="text/plain")
    # Js Data : {"name":"abhijeet rastogi","roll_no", Event:["event1","event2, "event3", "event4", "event5"]}

@csrf_exempt
def event_push(request):
    
    try:
        db = EventTable.objects.filter(roll_no=request.body.decode("utf-8"))

        event_list = [x.event for x in db]
        position_list = [x.position for x in db]

        print(event_list)
        print(position_list)


        dic = {"event":event_list, "position":position_list}
        ls = [dic]
        responseText = str(ls)[1:-1]

        return HttpResponse(responseText, content_type = "text/plain")
    except Exception as e:
        print(e)

@csrf_exempt
def sendnames(request):
    
    js = json.loads(request.body.decode("utf-8"))
    db = EventTable.objects.filter(event = js["event"])
    
    responseArray = []

    for i in db:
        studentDic = {}
    
        dbObj = StudentProfile.objects.filter(roll_no = str(i.roll_no))
        if dbObj[0].gender == js["gender"]:
            studentDic['roll_no'] = str(dbObj[0].roll_no)
            studentDic['name'] = str(dbObj[0].name)
            studentDic['year'] = str(dbObj[0].year)
            studentDic['branch'] = str(dbObj[0].branch)
            studentDic['position'] = i.position
            studentDic['college'] = str(dbObj[0].college)
            responseArray.append(studentDic)

    dic = {"student":responseArray}
    ls = [dic]
    dataPacket = str(ls)[1:-1]
    print(dataPacket)

    return HttpResponse(dataPacket, content_type = "text/plain")
        
@csrf_exempt
def updateShortList(request):
    requestData = json.loads((request.body.decode('utf-8')))
    for dataResource in requestData:
        EventTable.objects.filter(event = dataResource['event'], roll_no = dataResource['roll_no']).update(position = dataResource['position'])
    return HttpResponse("Success", content_type = "text/plain")

@csrf_exempt
def updatePositionList(request):
    requestData = json.loads((request.body.decode('utf-8')))
    for dataResource in requestData:
        EventTable.objects.filter(event = dataResource['event'], roll_no = dataResource['roll_no'], position = dataResource['qualified']).update(position = dataResource['position'])
    return HttpResponse("Success", content_type = "text/plain")

@csrf_exempt
def sendMail(request):
    
    email = request.body.decode("utf-8")
    print(email)
    obj = EmailMessage("Athletic Meet Registeration","666666", to=[email])
    return HttpResponse("666666", content_type = "text/plain")

    

