from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainPage_loggedOut_View, name = 'mainpage_loggedOut'),
    path('templates/login.html', views.loginPageView, name = 'login'),
    path('templates/courseOffered.html', views.courseOfferedPageView, name='courseOffered'),
    path('templates/createCourse.html', views.createCoursePageView, name='createCourse'),
    path('templates/manageCourse.html', views.manageCoursePageView, name='manageCourse'),
    path('templates/course_instructor.html', views.course_InstructorPageView, name = 'courseInstructor'),
    path('templates/manageQuiz.html', views.manageQuizPageView, name = 'manageQuiz'),
    path('templates/manageComponents.html', views.manageComponentPageView, name = 'manageComponent'),
    path('templates/insertComponent.html', views.insertComponentPageView, name= 'insertComponent'),
    path('templates/component_list.html', views.manageComponentPageView),
    path('saveModule', views.saveModule),
    path('saveQuiz', views.saveQuiz),
    path('saveComponent', views.saveComponent),

    path('templates/studyModule.html', views.studyModule, name='studyModule'),
    path('templates/studyModule_course1.html', views.studyModule_course1, name = 'studyModule_course1'),
    path('studyComponents', views.studyComponents),
]