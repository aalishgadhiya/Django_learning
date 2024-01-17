from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    DATA = {
        "title": "Django Practice Site",
        "d":"HELLO,OP!!!!!!",
        "list":["alish","ayush","parth","meet"],
        "student_details":[
            {"id":1,'name':"abc"},
            {"id":2,'name':"test"},
        ],
        "numbers":[10,20,30,40,50]
    }
    return render(request,"index.html",DATA)


def course(request,id):
    return HttpResponse(id)

def aboutus(request):
    return render(request,"aboutus.html")
