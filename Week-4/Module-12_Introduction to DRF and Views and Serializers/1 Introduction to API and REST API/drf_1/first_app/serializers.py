from rest_framework import serializers
from .import models

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.StudentData
        fields = '__all__'