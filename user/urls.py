
from django.urls import path,include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('user/register-user-event',register_user_event_Api,name='register_user_event_Api' ),
    
]
