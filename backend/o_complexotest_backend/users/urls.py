from django.urls import path

from .views import (
    RegistrationAPIView,
    LoginAPIView,
    MeAPIView,
)


urlpatterns = [
    path('register', RegistrationAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),

    path('me', MeAPIView.as_view(), name='user-me'),
]
