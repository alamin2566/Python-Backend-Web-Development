from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Feature


# Create your view here
#def index(request):

     ##return HttpResponse('<h1>Hi,Welcome</h1>')
    ##return render(request,'index.html')
   #name='Ali'
   #return render(request,'index.html',{'name':name})
    # Context dictionary
   # context = {
        #'name': 'Ali Naqi',
        #'subject': 'python',
        #'age': '29',  
        #'nationality': 'pakistani' 
    #}

   # return render(request, 'index.html') #context)  # Proper indentation
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already used')   
                return redirect('register')  

            elif User.objects.filter(username=username).exists():  
                messages.info(request, 'Username Already used')
                return redirect('register')  

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Passwords do not match')  
            return redirect('register')
    else:
     return render(request, 'register.html')
def login(request):
    if request.method == 'POST':  
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credential Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def counter(request):
        word=request.POST['text']
        amount_of_words=len(word.split())
        return render(request, 'counter.html',{'amount':amount_of_words})  # Proper indentation


def index(request):
      features=Feature.objects.all()
      return render (request,'index.html',{'features':features})

def post(request,id):
    return render(request,'post.html',{'id':id})