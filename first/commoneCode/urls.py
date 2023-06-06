from django.urls import path
from . import views



urlpatterns = [
    path("login/", views.Login, name = "login"),
    path("signup/", views.SignUp, name = "signup"),
    path("dashboard/", views.Dashboard, name = "dashboard"),
    path("upload/", views.Upload, name = "upload"),
]