from django.http import HttpResponse
from django.shortcuts import render

def home(rqst):
    # return HttpResponse('<h1><b>Home Page</b></h1>')
    return render(rqst,'home.html')