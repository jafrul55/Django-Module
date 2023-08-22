from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    publication_date = models.DateField()
    genre = models.CharField(max_length=50)
    availability_status = models.BooleanField(default=True)
    num_available = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.title
    
class BookReservation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,null=False,blank=False)
    reservation_date = models.DateTimeField(auto_now_add=True)
    notification_status = models.BooleanField(default=False)
    
    
class BookBorrowing(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,null=False,blank=False)
    borrow_date = models.DateField(null=False,blank=False)
    return_date = models.DateField(null=False,blank=False)
    
class Wishlist(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)
    
    def __str__(self):
        return f"Wishlist of {self.user.username} "
    