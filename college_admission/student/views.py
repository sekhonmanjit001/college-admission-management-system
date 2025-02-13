from django.shortcuts import render

def view_name (request):
    return render(request,"landingPage.html")
# Create your views here.
def signUp_register(request):
    return render(request,"Registration_student.html")
