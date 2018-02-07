from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json 
import csv
from .models import LoginTable, StudentProfile, EventTable, RollNo
import mimetypes
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import os
import time
import random


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
                    dic = {
                        'name':studentObj.name,
                        'roll_no':studentObj.roll_no,
                        'role':studentObj.role,
                        'gender':studentObj.gender,
                        'branch':studentObj.branch,
                        'CCET':studentObj.college,
                        'event_type':studentObj.event_type,
                        'event_year':studentObj.event_year
                    }
                else:
                    dic = {'role':str(i.role)}
            print(dic)
            ls = [dic]
            responseText = str(ls)[1:-1]

        except ObjectDoesNotExist:
            responseText = ''
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

        if checkValidRollNo((str(js["roll_no"]).upper())):
            print(ObjectDoesNotExist)
            print("Hell")
            dbRoll = RollNo.objects.filter(roll_no=str(js['roll_no']).upper())
            name = dbRoll[0].name
            dbObj.name = str(name)
            dbObj.roll_no = str(js["roll_no"])
            dbObj.branch = str(js["branch"])
            dbObj.semester = str(js["semester"])
            dbObj.year = str(js["year"])
            dbObj.email = str(js["email"])
            dbObj.mobile = str(js["mobile"])
            dbObj.role = str(js["role"])
            dbObj.gender = str(js["gender"])
            dbObj.college = str(js["college"])
            dbObj.event_type = str(js["event_type"])
            dbObj.event_year = time.strftime("%Y")
            dbObj.save()

            loginObj.password =str(js["roll_no"])
            loginObj.username = str(js["roll_no"])
            loginObj.role = str(js["role"])
            loginObj.save()
            
            return HttpResponse("success", content_type= "text/plain")
        else :
            return HttpResponse("Can't find Roll No in the records", content_type = "text/plain")

    except :
        return HttpResponse("Please Update Your App or Try After sometime", content_type = "text/plain")

def checkValidRollNo(roll):
    
    print("In Validation Shitt !! ")
    try:
        db = RollNo.objects.get(roll_no = roll)
        return True
    except:
        print("Hello")
        return False

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

        if js['event_type'] == "Inter Year":
            jsArray = js['event']
            dbObj = EventTable.objects.filter(roll_no = str(js["roll_no"]))
            
            if(len(dbObj) < 8):
                
                for events in jsArray:
                    db = EventTable()
                    db.roll_no = str(js["roll_no"])
                    db.event = events
                    db.position = "Not Played"
                    db.event_type = str(js['event_type'])
                    db.save()
                
            else: 
                response_str = "Already have registered for events"
                for i in dbObj:
                    response_str = response_str + "   " +str(i.event)

            return HttpResponse(response_str, content_type="text/plain")

        elif js['event_type'] == "Athletic Meet":
            jsArray = js['event']
            dbObj = EventTable.objects.filter(roll_no = str(js["roll_no"]))
            list_registered = []
            for x in dbObj:
                list_registered.append(x)
            
            if(len(dbObj) <= 5):
                for i in jsArray:
                    if i not in list_registered:
                        db = EventTable()
                        print(i)
                        db.roll_no = js["roll_no"]
                        db.event = i
                        db.position = "Not Played"
                        db.save()
                response_str = "Check profile to see the registered Events"
            else: 
                response_str = "Already have registered for events"
                for i in dbObj:
                    response_str = response_str + "   " +str(i.event)

                return HttpResponse(response_str, content_type="text/plain")

    except Exception as e: 
        print(str(e))
        return HttpResponse(str(e), content_type="text/plain")
    # Js Data : {"name":"abhijeet rastogi","roll_no", Event:["event1","event2, "event3", "event4", "event5"]}

@csrf_exempt
def event_push(request):
    
    try:
        db = EventTable.objects.filter(roll_no=request.body.decode("utf-8"))

        event_list = [x.event for x in db]
        position_list = [x.position for x in db]
        event_type = [x.event_type for x in db]

        event_data = []
        for i in range(0, len(event_list)):
            event_data.append(str(event_list[i])+" | "+str(event_type[i]))


        print(position_list)
        print(event_type)


        dic = {"event":event_data, "position":position_list}
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
    pin = random.randint(100000, 999999)
    obj = EmailMessage("Athletic Meet Registeration",str(pin), to=[email])
    obj.send()

    

    return HttpResponse(str(pin), content_type = "text/plain")

@csrf_exempt
def reportGeneration(request):
    
    gender_mask = json.loads(request.body.decode('utf-8'))
    roll_no = []

    for gender in gender_mask['gender']:
        db = StudentProfile.objects.filter(gender = gender)
        for dbInstance in db:
            roll_no.append(dbInstance.roll_no)
        
    finalRolls = []
    for roll in roll_no:
        dbEvent = EventTable.objects.filter(roll_no = roll)
        for event in dbEvent:
            if str(event.position) in gender_mask['position']:
                db = StudentProfile.objects.filter(roll_no= roll)
                dic = {"name": str(db[0].name),
                    "roll_no":str(db[0].roll_no), 
                    "branch":str(db[0].branch),
                    "year":str(db[0].year),
                    "event":str(event.event),
                    "position":str(event.position)
                }
                finalRolls.append(dic)

    employ_data = open('./media/EmployData.csv', 'a')

    # create the csv writer object

    csvwriter = csv.writer(employ_data)

    count = 0
    for x in finalRolls:
        js= json.dumps(x)
        jsoe = json.loads(js)
        print(jsoe.keys()) 
        if(count == 0):
            header = jsoe.keys()
            csvwriter.writerow(header)
            count+=1
        csvwriter.writerow(jsoe.values())

    employ_data.close()

    return HttpResponse(str(finalRolls)[1:-1],content_type="text/plain")


def loadCsv(request):
    file = open("./media/CollegeCutList.csv", "r")
    reader = csv.reader(file)
    for i in reader:
        db = RollNo()
        if(i[0] != 0):
            db.roll_no = i[0]
            db.name = i[1]
        db.save()
    
    return HttpResponse("Data Successfully Loaded")