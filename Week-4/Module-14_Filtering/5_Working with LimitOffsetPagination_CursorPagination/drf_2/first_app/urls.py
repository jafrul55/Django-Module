from django.urls import include, path
from rest_framework import routers
from .views import ProductViewSet, ProductReviewViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='Product')
router.register('review', ProductReviewViewSet, basename='Product-Review')

urlpatterns = [
    path('', include(router.urls)),
    # path('api_auth/',include('rest_framework.urls'))
]
