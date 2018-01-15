from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

''' this modules were imported when we had to upload the files to the server '''
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import User
# Create your views here.

app_name = "loginform"

def login(request):
    context = {
                'message':"Empathy - Our goal is to unite this world",
            }
    # try:
    return render(request,'loginform/login.html',context)
    # except:
    #     return HttpResponse("Page Not Found Error 404")

def validate(request):
    try:
        obj = User.objects.filter(username = str(request.POST['username']))
        if obj.get(password = str(request.POST['pass'])) != "":
            return HttpResponse("Welcome Babes") 
        
    except Exception as err:
    
        context = {
            'message':" either the Username or the Password is wrong"
        }
        return render(request, "loginform/login.html", context)
        
def signup(request):
    return render(request, 'loginform/signup.html', {})
    
def dbentry(request):
    
    try:
        User.objects.get(username = request.POST['username'])
        return HttpResponse("Record Not Created")
    except:
        q = User()
        q.username = request.POST['username']
        q.roll_no = request.POST['roll']
        q.name = request.POST['name']
        q.password = request.POST['password']
        
        #  This is the part which is going to help us upload the file to the server.

        if request.FILES['pic']:
            myfile = request.FILES['pic']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            
        q.save()
        return HttpResponseRedirect(reverse("loginform:login"))

