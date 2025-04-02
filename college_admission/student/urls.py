from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.view_name),
    path('register', views.signUp_register),
    path('dashboard', views.dashboard),
    path('form', views.form_first),
    path('conformation', views.conformation),
    path('courses', views.courses),
    path('studentslist', views.studentslist),
    path('studentdashboard', views.studentdashboard),
    path('result', views.result),
    path('api/register', views.register),
    path('api/login', views.login_view),
]




