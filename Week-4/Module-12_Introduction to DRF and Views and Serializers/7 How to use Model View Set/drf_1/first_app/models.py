from django.db import models

# Create your models here.
class StudentData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    def __str__(self):
        return self.name
    
    
# one student can take multiple course
# One to Many
# Many to One
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(StudentData,on_delete=models.CASCADE,related_name='course',
    default=None)
    name = models.CharField(max_length=20)
    marks = models.IntegerField()
    def __str__(self):
        return f"{self.name} : {self.marks}"