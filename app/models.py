from django.db import models


class Car(models.Model):
    car_make = models.CharField(max_length=40)
    car_model = models.CharField(max_length=40)
    car_year = models.CharField(max_length=4)
    car_vin = models.CharField(max_length=20)
