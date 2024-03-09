from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.views import UserRegistration, Logout  # Corrected import statement

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user-registration'),
    path('login/', obtain_auth_token, name='user-login'),
    path('logout/', Logout.as_view(), name='user-logout'),
    # Add more URLs for other functionalities if needed
]
