from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainPage_loggedOut_View(request):
    return render(request, 'mainpage_loggedOut.html')
    
def loginPageView(request):
    return render(request, 'login.html')

