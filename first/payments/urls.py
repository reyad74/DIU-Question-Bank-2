
from django.urls import path
from . import views



urlpatterns = [
    path("bikash/", views.bk, name = "paymentone"),
    path("roket/", views.rk, name = "paymentwo"),
    path("pays/", views.payment_methods, name = "pays"),
]