from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.view_name),
    path('register', views.signUp_register),
]

