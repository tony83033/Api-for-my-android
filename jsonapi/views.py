from django.http import request
from django.shortcuts import render
from django.urls.conf import path
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from random import randrange




# Create your views here.

def home(request):
    a= randrange(6)
    mylist =[
        "https://www.youtube.com/watch?v=3-WHQzEO7KU",
        "https://www.youtube.com/watch?v=N7Sx9S31Cnk",
        "https://www.youtube.com/watch?v=FvmtcuBnD6M",
        "https://www.youtube.com/watch?v=FvmtcuBnD6M",
        "https://www.youtube.com/watch?v=FvmtcuBnD6M",
        "https://www.youtube.com/watch?v=WTQlEvEKNFU",
    
    ]
   
    mydata = {
        "image1": "https://source.unsplash.com/480x1210/?nature,human",
        "image2" : "https://source.unsplash.com/1070x201/?nature,water",
        "video": mylist[a]
    }
    
    return JsonResponse(mydata)


