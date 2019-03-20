from django.urls import path

from . import views 

urlpatterns = [
    path('', views.monkeyPageView, name = 'monkey'),
    path('not_monkey/', views.engineerPageView, name = 'engineer'),
]