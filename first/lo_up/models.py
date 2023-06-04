from django.db import models

# Create your models here.
class UploadedQuestion(models.Model):
    department = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    year = models.IntegerField()
    exam = models.CharField(max_length=100)
    file = models.FileField(upload_to='question_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
