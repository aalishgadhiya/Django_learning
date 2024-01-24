from django.db import models


class Blog(models.Model):
    blog_title = models.CharField(max_length=30)
    blog_dis  = models.TextField()  
    
class News(models.Model):
    news_title = models.CharField(max_length=20)
    news_dis = models.TextField()
    
    
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location  = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=(('IT','IT'),('Non IT','Non IT'),('Mobiles Phones','Mobiles Phones')))
    added_date = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
 
        
class Employee(models.Model):
    emoloyee_name = models.CharField(max_length=50)
    company_name = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    
    
    
class User_data(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=50)
    
        