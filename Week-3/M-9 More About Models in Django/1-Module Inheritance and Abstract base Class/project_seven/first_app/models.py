from django.db import models

# Create your models here.


class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    address = models.TextField()

    def __str__(self) -> str:
        return f"Roll: {self.roll} Name: {self.name}"
    
    
# Model Inheritance:
# 1.abstract base class 
# 2.multitable inheritance 
# 3.Proxy model 


# 1.abstract base class:
class CommonInfoClass(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    class Meta:  #For this meta class where abstract true
        abstract = True #it's never give me any object or model of the class
    
class StudentInfoModel(CommonInfoClass):
    roll = models.IntegerField()
    payment = models.IntegerField()
    section = models.CharField(max_length=20)
    
class TeacherInfoModel(CommonInfoClass):
    salary = models.IntegerField()
    

