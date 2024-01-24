from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from home.models import Blog
from home.models import News
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from home.models import Company,Employee
from home.serializer import CompanySerializer,EmployeeSerializer,RegisterSerializer,LoginSerializer
from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication







class LoginAPI(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
           return Response({'status':False,'message':serializer.errors}) 
       
        print("-----------------------",serializer.data)
        user = authenticate(username = serializer.data['username'],email=serializer.data['email'],password=serializer.data['password'])
        
        if not user:
            return Response({'status':False,'message':'invalid credentials'}) 

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'status':True,'message':'user login','token':token.key})
        


class RegisterAPI(APIView):
    
    def post(self,request):
        data =request.data
        serializer = RegisterSerializer(data=data)  
        
        if not serializer.is_valid():
           return Response({'status':False,'message':serializer.errors}) 
       
        serializer.save()
        return Response({'status':True,'message':'user created'})         


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
    blogData = Blog.objects.all()
    data={
        "blogData":blogData
    }
    return render(request,"blog.html",data)



def newsPage(request):
    newsData = News.objects.all()
    data={
        'newsData':newsData
    }
    return render(request,"news.html",data)


def newsdetailsPage(request,newsid):
    newsData = News.objects.get(id=newsid)
    data={
        'newsData':newsData
    }
    return render(request,"detailNews.html",data)


@api_view(['POST','GET','PATCH'])
def hello_world_api(request):
    print(request.method)
    data =request.data
    print("****------")
    print(data['name'])
    return Response({'status' : 200,'message':f'hello world, this is a {request.method} method'})  
    # if request.method == "POST":
    #     return Response({'status' : 200,'message': 'hello world, this is a Post Method'})
    # elif request.method == "GET":
    #     return Response({'status' : 200,'message': 'hello world, this is a Get Method'})
    # elif request.method == "PATCH": 
    #     return Response({'status' : 200,'message':'hello world, this is a patch method'})   
    
    
  
  
# @api_view(['GET','POST','PATCH','DELETE'])  
# def CompanyDetails(request):
#     if request.method == "GET":
#         obj = Company.objects.all()
#         serializer = CompanySerializer(obj,many=True)
#         return Response(serializer.data) 
#     elif request.method == "POST":
#         data = request.data
#         serializer = CompanySerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)   
#     elif request.method == "PATCH":
#         data = request.data 
#         obj = Company.objects.get(company_id = data['company_id'])
#         serializer = CompanySerializer(obj,data=data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     else:
#         data  = request.data 
#         obj = Company.objects.get(company_id = data['company_id'])
#         obj.delete()
#         return Response({'message':'company_details deleted'})
    
    
    

class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        print(f"get employee of {pk} company")
        company = Company.objects.get(pk=pk)
        emp = Employee.objects.filter(company_name=company)
        emp_serializer = EmployeeSerializer(emp,many=True,context={'request':request})
        return Response(emp_serializer.data)
        
    
class EmplyoeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
    def list(self,request):
        search =request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(emoloyee_name__startswith =search) 
            
        serializer = EmployeeSerializer(queryset,many=True)     
        return Response({'status':200,'data':serializer.data})
        
    
    
    
        