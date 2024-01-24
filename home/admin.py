from django.contrib import admin
from home.models import Blog,News,Employee,User_data


class BlogAdmin(admin.ModelAdmin):
    list_display=('blog_title','blog_dis')


class NewsAdmin(admin.ModelAdmin):
    list_display=('news_title','news_dis')

admin.site.register(Blog,BlogAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Employee)
admin.site.register(User_data)

