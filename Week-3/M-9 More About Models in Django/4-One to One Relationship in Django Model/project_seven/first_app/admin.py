from django.contrib import admin
from first_app.models import StudentModel,StudentInfoModel,TeacherInfoModel,EmployeeModel,ManagerModel,Friend,Me,Person,Passport
# Register your models here.
admin.site.register(StudentModel)
# admin.site.register(StudentInfoModel)
# admin.site.register(TeacherInfoModel)
# admin.site.register(EmployeeModel)
# admin.site.register(ManagerModel)

#You can use @admin.register to see value perfectly:
# @admin.register(EmployeeModel)
# class EmployeeModelAdmin(admin.ModelAdmin):
#     list_display = ['id','name','city','designation']
    
    
# @admin.register(ManagerModel)
# class ManagerModelAdmin(admin.ModelAdmin):
#     list_display = ['id','name','city','designation','take_interview','hiring']


#Both class work for proxy model.friend class also give attendence of me
# @admin.register(Friend)
# class FriendModelAdmin(admin.ModelAdmin):
#     list_display = ['id','school','section','attendence','hw']
    
# @admin.register(Me)
# class MeModelAdmin(admin.ModelAdmin):
#     list_display = ['id','school','section','attendence','hw']

#For oneToone Relations:
@admin.register(Person)
class personModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','email']
    
@admin.register(Passport)
class PassportModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','pass_number','page','validity']
    
    




