from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer,ProfileUpadteSerializer,PasswordUpdateSerializer,UserUpdateSerializer
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import CustomUser
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework.authentication import TokenAuthentication  


class UserViewSet(APIView):
    '''Only admin can add and manage user and send creadentials via mail'''

    permission_classes = [IsAdminUser]

    def get(self, request):
        user = CustomUser.objects.all()
        serializer = UserSerializer(user,many=True)
        print('user: ', user)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer =UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        user = get_object_or_404(CustomUser,pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        user =get_object_or_404(CustomUser, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(APIView):
    '''Customer and Admin both login functionality.'''
    def post(self, request):
        email = request.data.get('email')
        print('email: ', email)
        password = request.data.get('password')
        print('password: ', password)
        
        user = authenticate(request, username=email, password=password)
        print('user: ', user)
        
        if user is not None:
            login(request,user)
            return Response({'message':'Login successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'error':'Invalid email or password, Please enter correct.'},status=status.HTTP_400_BAD_REQUEST)


class ForgetPasswordView(APIView):
    '''Customer forget password and reset password link send via mail to user and using that customr can set new password.'''
    def post(self,request):
        email = request.data.get('email')
        user = get_object_or_404(CustomUser,email=email)

        token = default_token_generator.make_token(user)

        reset_url = f"http://127.0.0.1:8000/reset-password/{user.pk}/{token}/"
        send_mail(
            subject="Password Rest Request",
            message=f"Please click the link to reset your password: {reset_url}",
            from_email="gam.globaliasoft@gmail.com",
            recipient_list=[user.email],
        )
        return Response({'message':'Password reset link'}, status=status.HTTP_200_OK)

class ResetPasswordView(APIView):
    '''Customer can reset password using old password and set new password for them.'''
    def post(self,request,pk,token):
        user = get_object_or_404(CustomUser,pk=pk)

        if default_token_generator.check_token(user,token):
            new_password = request.data.get('new_password')
            user.set_password(new_password)
            user.save()
            return Response({'message':'Password has been reset successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'error':'Invalid or expired token'},status=status.HTTP_400_BAD_REQUEST)
        

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        user = request.user
        serializer = ProfileUpadteSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self, request):
        user = request.user
        serializer = ProfileUpadteSerializer(user,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    

class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self,request):
        serializer = PasswordUpdateSerializer(data=request.data, context={'request':request})
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Passwordupdated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
        
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        logout(request)
        return Response({"message":"Successfully Logged Out!"}, status=status.HTTP_200_OK)        