
from django.urls import path
from . import views



urlpatterns = [
    path("", views.product, name = "productpage"),
    path("recent/", views.details),
    path("su/",views.send),
]