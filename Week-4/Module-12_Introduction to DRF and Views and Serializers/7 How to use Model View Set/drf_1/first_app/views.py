from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers
from rest_framework import generics
from rest_framework import viewsets

# You can get,post using this small code
# class StudentListCreateView(generics.ListCreateAPIView): #get,post
#     queryset = models.StudentData.objects.all()
#     serializer_class = serializers.StudentSerializers

# You can get,update,delete
# class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView): #get,post,delete
#     queryset = models.StudentData.objects.all()
#     serializer_class = serializers.StudentSerializers
# ----------------------------------------------------------------
# You can shortcut much more using model_view_set
# class StudentViewSet(viewsets.ModelViewSet): #You can edit and update value
#     queryset = models.StudentData.objects.all()
#     serializer_class = serializers.StudentSerializers

class StudentViewSet(viewsets.ReadOnlyModelViewSet): #You only read value but cannot update
    queryset = models.StudentData.objects.all()
    serializer_class = serializers.StudentSerializers



    
    

# You can use it to make hyperlink of any course
class CourseListCreateView(generics.ListCreateAPIView): #get,post
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializers

# You can get,update,delete
class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView): #get,post,delete
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializers

# class StudentView(APIView):
#     def get(self, request):
#         student_data = models.StudentData.objects.all()
#         serializer = serializers.StudentSerializers(student_data, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = serializers.StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class StudentDetailView(APIView):
#     def get(self, request, pk, format=None):
#         student_data = models.StudentData.objects.get(pk=pk)
#         serializer = serializers.StudentSerializers(student_data)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         student_data = models.StudentData.objects.get(pk=pk)
#         serializer = serializers.StudentSerializers(student_data, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         student_data = models.StudentData.objects.get(pk=pk)
#         student_data.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)