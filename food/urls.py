from django.urls import path , include
from rest_framework import routers
from .views import FoodViewSet

router = routers.DefaultRouter()
router.register(r'orders', FoodViewSet)

urlpatterns = [
    path('', include(router.urls)) ,
]
