from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2) #12.56
    def __str__(self):
        return self.name
    
class ProductReview(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #when object will be created that time will show
    update_at = models.DateTimeField(auto_now=True) #When user edit review that time will show
    
    class Meta:
        unique_together = ('product','user') #One user can only comment one
    def __str__(self):
        return f"{self.user.username} - {self.product.name} Rating: {self.rating}"
        
    
    
