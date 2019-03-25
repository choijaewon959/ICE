from django.urls import path

from . import views 

urlpatterns = [
    path('', views.mainPage_loggedOut_View, name = "mainpage_loggedOut"),
    path('templates/login.html', views.loginPageView, name = 'login'),
    path('templates/courseOffered.html', views.courseOfferedPageView, name='courseOffered'),
    path('templates/createCourse.html', views.createCoursePageView, name='createCourse'),
    path('templates/manageCourse.html', views.manageCoursePageView, name='manageCourse'),
    path('templates/course_instructor.html', views.course_InstructorPageView, name = 'courseInstructor'),
    path('templates/manageQuiz.html', views.manageQuizPageView, name = 'manageQuiz'),
    path('templates/manageComponents.html', views.manageComponentPageView, name = 'manageComponent'),
    path('templates/insertComponent.html', views.insertComponentPageView, name= 'insertComponent'),
]