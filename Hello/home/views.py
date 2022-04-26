from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
from home.models import *
from django.contrib import messages

# Create your views here.
def entryPage(request):
    return render(request, 'entryPage.html')

def studentLogin(request):
    return render(request, 'studentLogin.html')

def studentDashboard(request):
    return render(request, 'studentDashboard.html')

def adminDashboard(request):
    return render(request, 'adminDashboard.html')

def adminLogin(request):
    return render(request, 'adminLogin.html')
    
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")
    
def documentation(request):
    return render(request, 'documentation.html')

def faqs(request):
    return render(request, 'faqs.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
