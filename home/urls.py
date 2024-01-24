from django.urls import path,include
from home import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'company', views.CompanyViewSet)
router.register(r'employee', views.EmplyoeeViewSet)

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
    path("first/hello",views.hello_world_api),
    path("api/register-user",views.RegisterAPI.as_view()),
    path("api/login-user",views.LoginAPI.as_view()),
    # path("company-details/",views.CompanyDetails),
    
    path('api/', include(router.urls)),

]
 