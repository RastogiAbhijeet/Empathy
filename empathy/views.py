from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json 
from .models import LoginTable

# Create your views here. 

@csrf_exempt 
def validate(request):
    # Login Validation - 
    #     Checkes whether the received username and password are valid or not
    
    js = json.loads(request.body.decode('utf-8'))
    userName = js['Username'] 
    passWord = js['Password']
    print("Username : "+userName+"Password : " + passWord)
    try:
        dbObj = LoginTable.objects.filter(username = userName)
        print(dbObj)
        try:
            dbObj.get(password = str(passWord))
            dic = {'message':'He he','name':'Abhijeet', 'roll_no':'CO15302', 'role':'student','gender':'male'}

            ls = [dic]
            responseText = str(ls)[1:-1]

        except:
            responseText = 'Check either username or password is incorrect'

        return HttpResponse(responseText, content_type="text/plain")
    except:     
        return HttpResponse("No User Found", content_type="text/plain")