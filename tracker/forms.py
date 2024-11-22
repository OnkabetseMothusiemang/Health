from django import forms
from .models import MealLog, WorkoutLog, WaterLog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



class MealLogForm(forms.ModelForm):
    class Meta:
        model = MealLog
        fields = ['meal', 'calories']

class WorkoutLogForm(forms.ModelForm):
    class Meta:
        model = WorkoutLog
        fields = ['workout_type', 'duration', 'calories_burned']

class WaterLogForm(forms.ModelForm):
    class Meta:
        model = WaterLog
        fields = ['water_amount']
