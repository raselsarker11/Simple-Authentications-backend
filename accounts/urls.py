from django.urls import path
from .views import UserRegisterViewSet, UserLoginViewSet

urlpatterns = [
    path('register/', UserRegisterViewSet.as_view(), name='signup-page'),
    path('login/', UserLoginViewSet.as_view(), name='login-page'),
]
