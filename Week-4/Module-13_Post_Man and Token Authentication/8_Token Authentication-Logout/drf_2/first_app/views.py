from django.shortcuts import render
from rest_framework import viewsets
from . import models,serializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from . import permissions


# For Doing CRUD Operation
# Create,Read,Update,Delete
class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated] #This will use when it will be authenticated user
    # permission_classes = [IsAuthenticatedOrReadOnly]#This will use to see product but cannot edit product
    permission_classes = [permissions.AdminOrReadOnly] #Admin can read and edit/Custom Permission
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers
    
# For Doing CRUD Operation
# Create,Read,Update,Delete
class ProductReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.ReviewerOrReadOnly] #Reviewers can check read but can not change/Custom Permission
    queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ProductReviewSerializers
