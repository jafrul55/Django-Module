from decimal import Decimal
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import (MinValueValidator,MaxValueValidator)
from django.db import models
from .managers import UserManager

class User(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True,null=False,blank=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self): #after creating account return email
        return self.email
   
    #Decorator:
    @property
    def balance(self):
        if hasattr(self,'account'): #jodi account take then return balance
            return self.account.balance
        return 0