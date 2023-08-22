from django.db import models

# Create your models here.
class StudentData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    roll = models.IntegerField()