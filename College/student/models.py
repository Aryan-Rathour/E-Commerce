from django.db import models

class student(models.Model):
    student_id=models.IntegerField(max_length=10,unique=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField(max_length=10)
    grade=models.CharField(max_length=5)
    
    def __str__(self):
        return self.first_name

