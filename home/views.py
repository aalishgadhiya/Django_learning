from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect


def index(request):
    DATA = {
        "title": "Django-Practice Site",
        "d":"HELLO,OP!!!!!!",
        "list":["alish","ayush","parth","meet"],
        "student_details":[
            {"id":1,'name':"abc"},
            {"id":2,'name':"test"},
        ],
        "numbers":[10,20,30,40,50]
    }
    return render(request,"index.html",DATA)


# def course(request,id):
#     return HttpResponse(id)

def aboutus(request):
    output=0
    try:
        if request.method == "GET":
            output = request.GET.get('output')
    except:
        pass          
    DATA = {
        "title":"Django-Practice-Aboutus",
        "output":output
    }
    return render(request,"aboutus.html",DATA)



def formpage(request):
    finalans=0
    try:
       if request.method == "POST": 
        # n1 = int(request.GET.get('num1'))
        # n2 = int(request.GET.get('num2'))
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1+n2
            url=f"/about-us?output={finalans}"
            return HttpResponseRedirect(url)
    except:
        pass
    DATA = {
        "title":"Django-Practice-formus",
        "output":finalans
    }
    return render(request,"form.html",DATA)



def submitForm(request):
    try:
       if request.method == "POST": 
        # n1 = int(request.GET.get('num1'))
        # n2 = int(request.GET.get('num2'))
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1+n2
    except:
        pass    
    return HttpResponse(finalans)

    
def calculatorPage(request):
    n1=0
    n2=0
    finalans = 0
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get("num1"))
            n2 = eval(request.POST.get("num2"))
            opr = request.POST.get("opr")
            
            if opr == "+":
                finalans = n1+n2
            elif opr == "-":
                finalans = n1-n2 
            elif opr == "*":
                finalans = n1*n2        
            elif opr == "/":
                finalans = n1/n2 
                   
            print(finalans)
    except:
        pass
    
    DATA = {
        "output":finalans,
        "val_1":n1,
        "val_2":n2
    }
    return render(request,"calculator.html",DATA)
    
    
    
def blogPage(request):
    return render(request,"blog.html")