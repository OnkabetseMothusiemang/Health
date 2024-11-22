from django.shortcuts import render, redirect
from .forms import MealLogForm, WorkoutLogForm, WaterLogForm
from django.shortcuts import render, redirect
from .models import MealLog, WorkoutLog, WaterLog
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the user, including hashed password
            return redirect('login')  # Redirect to login page after registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Logs the user in
            return redirect('dashboard')  # Redirect to dashboard after login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to the built-in login view

    user = request.user
    meals = MealLog.objects.filter(user=user)
    workouts = WorkoutLog.objects.filter(user=user)
    water_logs = WaterLog.objects.filter(user=user)

    total_calories = sum(meal.calories for meal in meals)
    total_calories_burned = sum(workout.calories_burned for workout in workouts)
    total_water = sum(log.water_amount for log in water_logs)

    context = {
        'meals': meals,
        'workouts': workouts,
        'water_logs': water_logs,
        'total_calories': total_calories,
        'total_calories_burned': total_calories_burned,
        'total_water': total_water,
    }
    return render(request, 'dashboard.html', context)



def log_meal(request):
    if request.method == 'POST':
        form = MealLogForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return redirect('dashboard')
    else:
        form = MealLogForm()
    return render(request, 'log_meal.html', {'form': form})

def log_workout(request):
    if request.method == 'POST':
        form = WorkoutLogForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('dashboard')
    else:
        form = WorkoutLogForm()
    return render(request, 'log_workout.html', {'form': form})

def log_water(request):
    if request.method == 'POST':
        form = WaterLogForm(request.POST)
        if form.is_valid():
            water_log = form.save(commit=False)
            water_log.user = request.user
            water_log.save()
            return redirect('dashboard')
    else:
        form = WaterLogForm()
    return render(request, 'log_water.html', {'form': form})
