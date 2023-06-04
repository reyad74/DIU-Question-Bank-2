from django.contrib import admin
from .models import laptop

# Register your models here.
admin.site.register(laptop)

class laptopAdmin(admin.ModelAdmin):
    list_display = ("password","laptop","email","about","text_area","check_box")