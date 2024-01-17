from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name = "home"),
    path("about-us",views.aboutus,name = "about-us"),
    # path("<slug:id>",views.course,name = "course")
]
