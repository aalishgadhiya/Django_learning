from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name = "home"),
    path("about-us",views.aboutus,name = "about-us"),
    path("form-page",views.formpage,name="form-page"),
    path("submit-form",views.submitForm,name="submit-form"),
    path("calculator-page",views.calculatorPage,name="calculator-page"),
    path("blog-page",views.blogPage,name="blog-page"),
    path("news-page",views.newsPage,name="news-page"),
    path("newsdetails-page/<newsid>",views.newsdetailsPage,name="newsdetails-page"),
    # path("<slug:id>",views.course,name = "course")
    path("first/hello",views.hello_world_api)
]
