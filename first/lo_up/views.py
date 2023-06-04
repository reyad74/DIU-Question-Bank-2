from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import UploadedQuestion




# This is the  user login functionality in Django.
def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User credentials are valid, log in the user
            login(request, user)
            return HttpResponseRedirect('/dashboard/')  # Redirect to the dashboard 
        else:
            # User credentials are invalid, handle the error
            error_message = "Invalid username or password."
            return render(request, "lo_up/login.html", {'error_message': error_message})

    return render(request, "lo_up/login.html")
    



# This is the  user registration functionality in Django.
def SignUp(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        checkbox = request.POST.get("checkbox")

        # Check if the passwords match
        if password1 == password2:
            # Create a new user
            new_user = User.objects.create_user(username=username, email=email, password=password1)
            new_user.save()

            # Redirect to a success page or login page
            return HttpResponseRedirect('/login/')
        else:
            # Passwords don't match, handle the error
            error_message = "Passwords do not match!"
            return render(request, "lo_up/signup.html", {'error_message': error_message})

    return render(request, "lo_up/signup.html")




# This is the dashboard

def Dashboard(request):
    return render(request, "lo_up/dashboard.html")






# Upload page
def Upload(request):
    if request.method == 'POST':
        department = request.POST.get('department')
        semester = request.POST.get('semester')
        year = request.POST.get('year')
        exam = request.POST.get('exam')
        file = request.FILES.get('file')

        question = UploadedQuestion(
            department=department,
            semester=semester,
            year=year,
            exam=exam,
            file=file
        )
        question.save()
        return HttpResponseRedirect('/dashboard/')  # Redirect to a success page after saving the data
    return render(request, "lo_up/upload.html")






