from django.urls import path
from .views import *
urlpatterns = [
    path('api/2015-12-25/',SimpleAPIView.as_view()),
    path('api/1451001600000/',SimpleAPIView.as_view()),
]