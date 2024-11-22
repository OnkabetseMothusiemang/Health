from django.urls import path, include
from tracker.views import register, custom_login  # Import views from the 'tracker' app

urlpatterns = [
    path('accounts/register/', register, name='register'),  # Registration page URL
    path('accounts/login/', custom_login, name='login'),    # Login page URL
    path('accounts/', include('django.contrib.auth.urls')),  # Default auth URLs
    path('', include('tracker.urls')),  # Include the 'tracker' app URLs
]
