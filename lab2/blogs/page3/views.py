from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_app(request):
    return HttpResponse("hello app")
