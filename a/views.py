from django.shortcuts import render , HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")
def login_(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user),
            messages.success(request,"Wellcome")
            return render(request,"contact.html")
        else:
            messages.info(request,"Invalid"),
            return render(request,'login.html')
           
    else:
        messages.info(request,"Invalid"),
        return render(request,'login.html')

    return render(request,'login.html')
def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password= request.POST['password']
        passwordre = request.POST['passwordre']
        if password== passwordre:
            if User.objects.filter(username=username).exists():
                print("username Taken")
            else:
                user = User.objects.create(username=username,password=password,email=email)
                user.save()
                print('user careated')
        # return redirect('/')
        else:
            print("Password is not macthichng")
            return render(request,'signup.html')
    return render(request,'signup.html')
def contact(request):
    return render(request,'contact.html')