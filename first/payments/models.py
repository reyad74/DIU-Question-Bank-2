from django.db import models

# Create your models here.
class Pay_method(models.Model):
    pay_id = models.IntegerField()
    pay_option = models.CharField(max_length = 25)
    min_pay = models.IntegerField()