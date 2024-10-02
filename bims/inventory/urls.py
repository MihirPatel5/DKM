from django.urls import path
from .views import (UserViewSet, InventoryItemView, ForgetPasswordView, 
                    LogoutView, PasswordChangeView, UserProfileView, 
                    CostSheetView, QuantitySheetView, ProjectView,LoginView)

urlpatterns = [ 
    path('user/', UserViewSet.as_view()),
    path('users/<int:pk>/', UserViewSet.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('profile/password/', PasswordChangeView.as_view()),
    path('forgot-password/', ForgetPasswordView.as_view()),
    path('projects/', ProjectView.as_view(), name="projects"),
    path('projects/<int:pk>/', ProjectView.as_view(), name='project-details'),
    path('projects/<int:project_id>/quantity-sheets/', QuantitySheetView.as_view(), name='quantity-view'),
    path('projects/<int:project_id>/cost-sheets/', CostSheetView.as_view(), name='cost-view'),
    path('projects/<int:project_id>/inventory-items/', InventoryItemView.as_view(), name='inventory-items'),
]
