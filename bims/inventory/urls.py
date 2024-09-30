from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,LoginView,ForgetPasswordView,LogoutView,PasswordChangeView,UserProfileView,CostSheetView,QuantitySheetView,ProjectView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [ 
    path('user/', UserViewSet.as_view()),
    path('users/<int:pk>/',UserViewSet.as_view()),
    path('login/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view()),
    path('profile/',UserProfileView.as_view()),
    path('profile/password/',PasswordChangeView.as_view()),
    path('forgot-password/',ForgetPasswordView.as_view()),
    path('projects/',ProjectView.as_view(),name="projects"),
    path('projects/<int:pk>/',ProjectView.as_view(),name='project-details'),
    path('projects/<int:project_id>/quantity-sheets/',QuantitySheetView.as_view(),name='quantity-view'),
    path('projects/<int:project_id>/cost-sheets/',CostSheetView.as_view(),name='cost-view')
]
