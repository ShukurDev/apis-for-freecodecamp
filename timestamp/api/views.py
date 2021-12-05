from django.shortcuts import render
from .models import SimpleAPI
from .serializers import SimpleSerializer
from rest_framework.generics import ListAPIView


# Create your views here.

class SimpleAPIView(ListAPIView):
    queryset = SimpleAPI.objects.all()
    serializer_class = SimpleSerializer



