from django.db import models

# Create your models here.

class BookStoreModel(models.Model):
    CATEGORY = (
        ('Mystery', 'Mystery'),
        ('Thriller', 'Thriller'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Humor', 'Humor'),
        ('Horror', 'Horror'),
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30,choices= CATEGORY)
    first_published = models.DateTimeField(auto_now_add = True) #First time it will show published date
    last_published = models.DateTimeField(auto_now = True) #After that all updates date will show here(last update)
