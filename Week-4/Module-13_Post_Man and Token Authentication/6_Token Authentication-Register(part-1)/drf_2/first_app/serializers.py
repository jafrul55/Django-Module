from rest_framework import serializers
from . models import Product,ProductReview

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'