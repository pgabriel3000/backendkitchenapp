from django.urls import path , include
from rest_framework import routers
from .views import DrinkViewSet

router = routers.DefaultRouter()
router.register(r'drink', DrinkViewSet)

urlpatterns = [
    path('', include(router.urls)) ,
]
