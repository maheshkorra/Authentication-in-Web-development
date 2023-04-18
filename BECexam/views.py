from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
    return render(request, "authentication/homepage.html") #HttpResponse("hello home is working")
def index(request):
    return render(request, "authentication/index.html")
def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST['pass1']
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            #messages.success(request, "Hello msg "+fname)
            return render(request, "authentication/index.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credential")
            return render(request, "authentication/signinpage.html")
    return render(request, "authentication/signinpage.html")

def signup(request):
    if request.method == "POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST.get('email')
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "your account created successfully")
 
        return redirect('signin')

    return render(request, "authentication/signuppage.html")
def signuppagecss(request):
    return render(request, "authentication/signuppage.css")

def signout(request):
    return render(request, "authentication/homepage.html")
