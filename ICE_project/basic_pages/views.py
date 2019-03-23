from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainPage_loggedOut_View(request):
    return render(request, 'mainpage_loggedOut.html')
    
def loginPageView(request):
    return render(request, 'login.html')

def courseOfferedPageView(request):
    return render(request, 'courseOffered.html')

def createCoursePageView(request):
    return render(request, 'createCourse.html')

def manageCoursePageView(request):
    return render(request, 'manageCourse.html')

def course_InstructorPageView(request):
    return render(request, 'course_instructor.html')

def manageQuizPageView(request):
    return render(request, 'manageQuiz.html')

def manageComponentPageView(request):
    return render(request, 'manageComponents.html')

def insertComponentPageView(request):
    return render(request, 'insertComponent.html')