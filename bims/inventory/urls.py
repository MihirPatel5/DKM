from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,LoginView,ForgetPasswordView,LogoutView,PasswordChangeView,UserProfileView


urlpatterns = [ 
    path('user/', UserViewSet.as_view()),
    path('users/<int:pk>/',UserViewSet.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/',UserProfileView.as_view()),
    path('profile/password/',PasswordChangeView.as_view()),
    path('forgot-password/',ForgetPasswordView.as_view()),
]
