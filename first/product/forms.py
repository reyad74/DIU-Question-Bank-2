from django.core import validators
from django import forms

class RecentProduct(forms.Form):
    password = forms.CharField(widget = forms.PasswordInput)
    laptop = forms.CharField(label= "Enter your laptop name: ")
    email = forms.EmailField(initial = "shuvo-sir@gmail.com")
    about = forms.CharField(help_text = "Describe about your laptop")
    text_area = forms.CharField(widget = forms.Textarea(attrs={"rows": 15, "cols": 50}))
    check_box = forms.CharField(widget = forms.CheckboxInput)
