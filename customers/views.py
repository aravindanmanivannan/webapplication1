from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
    return render(request,'customers/login.html')

def hi1(request):
    return render(request,'customers/signup.html')