from django.shortcuts import render
from product.forms import RecentProduct
from django.http import HttpResponseRedirect
from .models import laptop


# Create your views here.
def product(request):
    return render(request, "Product/product.html")



def send(request):

    return render(request, "Product/submit.html")


def details(request):
    if request.method == "POST":
        frm = RecentProduct(request.POST)
        if frm.is_valid():
            pas = frm.cleaned_data["password"]
            lap = frm.cleaned_data["laptop"]
            eml = frm.cleaned_data["email"]
            abt = frm.cleaned_data["about"]
            tex = frm.cleaned_data["text_area"]
            che = frm.cleaned_data["check_box"]
            buy = laptop(password = pas, laptop = lap, email = eml, about = abt, text_area = tex, check_box = che)
            buy.save()  
        return HttpResponseRedirect("/pro/su")

    else:
        frm = RecentProduct(auto_id= True, label_suffix= " ")
        print("GET statement")

    return render(request, "Product/recent.html",{"form" : frm})