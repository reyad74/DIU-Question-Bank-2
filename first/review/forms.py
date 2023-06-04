from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class BuildingAdd(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","first_name","last_name"]



class ModifySuccessForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "date_joined", "last_login", "is_staff", "is_active"]
