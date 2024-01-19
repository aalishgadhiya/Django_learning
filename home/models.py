from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length=30)
    blog_dis  = models.TextField()  
    
    
class News(models.Model):
    news_title = models.CharField(max_length=20)
    news_dis = models.TextField()
    
    