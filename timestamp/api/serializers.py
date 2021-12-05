from rest_framework import serializers
from .models import SimpleAPI


class SimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleAPI
        fields = '__all__'


