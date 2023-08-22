from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.contrib import auth

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('email must be set')
        email = self.normalize_email(email) #Consider every email as normal
        #Max@gmail.com
        #max@gmail.com
        user = self.model(email=email,**extra_fields)
        user.set_password(password) #to set password
        user.save(using = self._db) #to save user instance in database
        return user
    
    def create_user(self,email=None,password= None,**extra_fields):
        extra_fields.setdefault('is_staff',False) #So that no one access
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have the is_staff True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have the is_superuser True")
        return self._create_user(email,password,**extra_fields)
            
        
        
        
    

