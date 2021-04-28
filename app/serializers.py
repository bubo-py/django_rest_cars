from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'car_make', 'car_model', 'car_vin')
