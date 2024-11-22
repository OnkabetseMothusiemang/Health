from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    daily_water_goal = models.FloatField(default=2.0)  # in liters

class MealLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    meal = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()

class WorkoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    workout_type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()  # in minutes
    calories_burned = models.PositiveIntegerField()

class WaterLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    water_amount = models.FloatField()  # in liters
