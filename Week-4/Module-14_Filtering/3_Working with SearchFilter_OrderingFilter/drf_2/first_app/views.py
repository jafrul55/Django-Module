from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from . import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# For Doing CRUD Operation
# Create,Read,Update,Delete
class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated] #This will use when it will be authenticated user
    # permission_classes = [IsAuthenticatedOrReadOnly]#This will use to see product but cannot edit product
    # Admin can read and edit/Custom Permission
    permission_classes = [permissions.AdminOrReadOnly]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers
    # filter_backends = [filters.SearchFilter]  #For Seraching
    # search_fields = ['name', 'description']

    filter_backends = [filters.OrderingFilter]  # For Ordering
    ordering_fields = ['price']


# For Doing CRUD Operation
# Create,Read,Update,Delete


class ProductReviewViewSet(viewsets.ModelViewSet):
    # Reviewers can check read but can not change/Custom Permission
    permission_classes = [permissions.ReviewerOrReadOnly]
    queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ProductReviewSerializers
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['rating', 'product', 'user__username']

    filter_backends = [filters.OrderingFilter]  # For Ordering
    ordering_fields = ['rating']
    # def get_queryset(self):
    #     queryset = models.ProductReview.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:
    #         # To support every (capital or smaller ) username ->icontains
    #         queryset = queryset.filter(user__username__icontains=username)
    #     return queryset
