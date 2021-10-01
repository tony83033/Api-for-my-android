from django.http import request
from django.shortcuts import render
from django.urls.conf import path
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.

def home(request):
    mydata = {
        "name": "sumit",
        "class" : "12",
        "age": "18"
    }
    return JsonResponse(mydata)


