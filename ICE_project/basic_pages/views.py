from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.db import transaction
import datetime 

from .models import Module, Course, Component, Quiz, Question, Text, Image

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
    mods = Module.objects.all()

    return render(request, 'course_instructor.html', {
        'mod_list': mods
    })

def studyModule(request):
    return render(request, 'enrolledCourses.html')

def manageQuizPageView(request):

    key = request.POST.get('k2')
    title = request.POST.get('title2')
    print(key)

    exist = Quiz.objects.filter(id=key)
    if(len(exist) < 1):
        q = Quiz(
            quiz_number_of_questions = 4,
            id = key,
            quiz_passingmark = 60,
            quiz_complete = False,
            module_id = key
        )
        q.save()

    #q = Quiz.objects.get(id=key)
    
    questions = Question.objects.filter(quiz_id=key)
    #for q in questions:
    #    print(q.questionTxt)
    return render(request, 'manageQuiz.html',{
        'ques': questions,
        'k2': key,
        'title2' : title
    })

def manageComponentPageView(request):
    key = request.POST.get('k')
    titles = request.POST.get('title')
    
    components = Component.objects.filter(module_id=key)
    print(len(components))
    print(key, ' module id')
    return render(request, 'component_list.html',{
        'components_list' : components,
        'k': key,
        'title' : titles
    })

def insertComponentPageView(request):
    return render(request, 'insertComponent.html')

def saveModule(request):
    r = request.POST
    m = Module()
    m.module_id = r['number']
    m.module_title = r['title']
    m.module_complete = False
    m.module_progress = 60
    m.course_id = '1'
    m.save()

    key = request.POST.get('k')
    titles = request.POST.get('title')
    
    components = Component.objects.filter(id=key)

    return HttpResponseRedirect('templates/course_instructor.html', {
        'components': components
    })

def studyModule_course1(request):
    m  = Module.objects.filter(course_id = '1')

    return render(request, 'studyModule_course1.html',{
        'modules': m,
        'coursename' : '1',
    })

def studyComponents(request):
    r = request.POST
    key = r.get('k')
    print('key', key)
    courseId = r.get('courseID')
    print('courseId' , courseId )

    m = Module.objects.filter(course_id=courseId)
    c = Component.objects.filter(module_id = m[0].id)
    q = Quiz.objects.filter(module_id=m[0].id)
    quest = Question.objects.filter(quiz_id=q[0].id)

    return render(request, 'studyComponents.html',{
        'components' : c,
        'question' : quest
    })
        

def saveQuiz(request):
    r = request.POST
    question = Question(
        question = r['questionTxt'],
        quiz_id = r['moduleNum'],
        choice1 = r['o1'],
        choice2 = r['o2'],
        choice3 = r['o3'],
        choice4 = r['o4'],
        answer = r['answer'],
    )
    question.save()
    return HttpResponseRedirect('templates/course_instructor.html')

def saveComponent(request):
    r = request.POST
    foriegnkey = r.get('moduleID')
    titles = r.get('title')
    #components = Component.objects.filter(id=foriegnkey)
    #print(components)

    print('key', foriegnkey)

    c= None
    if r.get('type') == 'text':
        c = Text(
            component_id= r.get('number'),
            component_type = 0,
            component_title = r.get('title'),
            component_creation_date = datetime.datetime.now(),
            component_lastUpdate_date = datetime.datetime.now(),
            module_id = foriegnkey,
            component_content = "empty"
        )
    elif r.get('type') == 'image':
        c = Image(
            component_id= r.get('number'),
            component_type = 0,
            component_title = r.get('title'),
            component_creation_date = datetime.datetime.now(),
            component_lastUpdate_date = datetime.datetime.now(),
            module_id = foriegnkey,
            component_content = "empty"
        )
    if c:
        c.save()

    #components = Component.objects.filter(id=foriegnkey)
    #print(Component)

    return HttpResponseRedirect('templates/course_instructor.html')

    # return render(request, 'component_list.html',{
    #     'components': components,
    #     'k': key,
    #     'title' : titles
    # })

class CourseViewAll(ListView):
    model = Course

