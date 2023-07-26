from django.db import models

from django.utils.translation import gettext_lazy as _

# Create your models here.

class Course(models.Model):
    title=models.CharField(max_length=300)
    duration=models.CharField(max_length=50, default="3 months")
    about_course=models.TextField()
    price=models.DecimalField(decimal_places=2, max_digits=10)
    start_date=models.DateField()
    end_date=models.DateField()

    def __str__(self):
        return self.title

GENDER_CHOICES=[
    ('Male','M'),
    ('Female', 'F')
]

class Student(models.Model):
    name=models.CharField(max_length=300)
    age=models.PositiveIntegerField()
    email=models.EmailField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name

class Admission(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    is_paid=models.BooleanField(default=False)

    def __str__(self, is_paid):
        if is_paid:
          return f'{self.student.name} registered'
        else:
               return f'{self.student.name} has not paid'
    
class Teacher(models.Model):
    first_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)

