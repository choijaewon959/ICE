from django.urls import path

from . import views 

urlpatterns = [
    path('', views.mainPage_loggedOut_View, name = "mainpage_loggedOut"),
    path('/templates/login.html', views.loginPageView, name = 'login'),
    path('/templates/courseOffered.html', views.courseOfferedPageView, name='courseOffered')
]