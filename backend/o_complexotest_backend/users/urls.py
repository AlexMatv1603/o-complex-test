from django.urls import path

from .views import (
    RegistrationAPIView,
    MeAPIView,
)


urlpatterns = [
    path('register', RegistrationAPIView.as_view(), name='register'),
    path('me', MeAPIView.as_view(), name='user-me'),
]
