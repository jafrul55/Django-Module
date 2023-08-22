from rest_framework import serializers
from .import models


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'
        
# One to many
# Student can choose multiple course   
class StudentSerializers(serializers.ModelSerializer):
    # One student can take multiple course
    course = CourseSerializers(many = True, read_only = True)
    class Meta:
        model = models.StudentData
        fields = '__all__'
   