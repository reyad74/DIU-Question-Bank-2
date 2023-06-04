from django.shortcuts import render, HttpResponseRedirect
from .forms import BuildingAdd, ModifySuccessForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def customer(request):
    return render(request, "Review/review.html")


# Registration
def building_form(request):
    if request.method == "POST":
        frm = BuildingAdd(request.POST)
        if frm.is_valid():
            frm.save()

    else:

        frm = BuildingAdd
    return render(request,"Review/building.html", {"form" : frm})



# Login
def login_form(request):
    if request.method == "POST":
        frm = AuthenticationForm(request=request, data = request.POST)
        if frm.is_valid():
            usern = frm.cleaned_data["username"]
            userp = frm.cleaned_data["password"]
            user = authenticate(username = usern, password = userp)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/rew/success')
    else:
        frm = AuthenticationForm()
    return render(request, "Review/login.html", {"form" : frm})



# Successfully Login
def login_success(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            frm = ModifySuccessForm(request.POST, instance=request.user)
            if frm.is_valid():
                frm.save()
        else:
            frm = ModifySuccessForm(instance = request.user)
        return render(request,"Review/success.html", {"form" : frm})
    else:
        return HttpResponseRedirect("/login/")        



# Log out
def logout_form(request):
    logout(request)
    return HttpResponseRedirect("/rew/login/")


# Password change using old password
def password_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            frm = PasswordChangeForm(data=request.POST, user=request.user)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request, frm.user)
                return HttpResponseRedirect('/rew/success')
        else:
            frm = PasswordChangeForm(user=request.user)
        return render(request, "Review/cpass.html", {"form" : frm})

    else:
        return HttpResponseRedirect("/rew/login/")