from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'SenseHome/home.html')


def about(request):
    return render(request,'SenseHome/classifier.html')

def signup(request):
    return render(request,'SenseHome/signup.html')
