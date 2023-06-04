from django.contrib import admin
from payments.models import Pay_method
# Register your models here.
class Pay_methodAdmin(admin.ModelAdmin):
    list_display = ("id","pay_id","pay_option","min_pay")

admin.site.register(Pay_method,Pay_methodAdmin)