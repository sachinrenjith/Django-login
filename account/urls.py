from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileView, UserProfileEdit

urlpatterns = [
  path('register/', UserRegistrationView.as_view(), name='register'),
  path('login/', UserLoginView.as_view(), name='login'),
  path('profile/',UserProfileView.as_view(),name='profile'),
  path('profileedit/',UserProfileEdit.as_view(),name='profileedit'),
  path('profileedit/<int:pk>/',UserProfileEdit.as_view(),name='profileedit'),
]

