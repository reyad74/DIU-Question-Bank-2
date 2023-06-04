from django.db import models

# Create your models here.
class laptop(models.Model):
     password = models.CharField(max_length=50)
     laptop = models.CharField(max_length=50)
     email = models.EmailField(max_length=50)
     about = models.CharField(max_length=50)
     text_area = models.CharField(max_length=50)
     check_box = models.CharField(max_length=50)
     
