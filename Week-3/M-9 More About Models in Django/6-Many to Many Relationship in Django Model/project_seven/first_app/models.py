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
    
    
# 2.multitable inheritance:
class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    designation = models.CharField(max_length=20)
    
    
class ManagerModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()
    
    
# 3.Proxy model: amar firend amar class attendence ta diya daba
#Friend clas ar sokol kaz me korta parba
#friend a kaz korla me ta chola jaba and me ta kaz korla friend ta chola jaba
class Friend(models.Model): #Amar friend az class a present acha
    school = models.CharField(max_length=40)
    section = models.CharField(max_length=10)
    attendence = models.BooleanField()
    hw = models.CharField(max_length=50)
    
class Me(Friend): #ami az class a zai nai
    class Meta:
        proxy = True
        # You can also filter data from big to small:
        ordering = ['id']
    


# 1. One to One Relationship in Django Model:
class Person(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    def __str__(self):
        return self.name
    
class Passport(models.Model):
    user = models.OneToOneField(to=Person, on_delete = models.CASCADE)
    pass_number = models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()
    
    
    
#2.One to many relationship:
#one to many or many to one in this case we use foreignkey
class Post(models.Model):
    user = models.ForeignKey(Person,on_delete=models.SET_NULL,null=True)
    post_cap = models.CharField(max_length=30)
    post_details = models.CharField(max_length=100)
    

#3.Many to Many relationship:
class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    class_name = models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    student = models.ManyToManyField(Student)
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    def student_list(self):
        return ",".join([str(i) for i in self.student.all()])

    
    
    

