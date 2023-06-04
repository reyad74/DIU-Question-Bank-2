
from django.shortcuts import render
from payments.models import Pay_method

# Create your views here.
def bk(requst):
    return render(requst, "Payments/payments1.html")

def rk(requst):
    return render(requst, "Payments/payments2.html")


def payment_methods(request):
    pay_m = Pay_method.objects.all()
    
    return render(request, "Payments/pay.html", {"pay" : pay_m})