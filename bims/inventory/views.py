from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer,ProfileUpdateSerializer,PasswordUpdateSerializer,ProjectSerializer,CategorySerializer,SubCategorySerializer,QuantitySheetSerializer,CostSheetSerializer
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import CustomUser,Project,QuantitySheet,CostSheet
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken


class UserViewSet(APIView):
    '''Only admin can add and manage user and send creadentials via mail.'''

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
            refresh = RefreshToken.for_user(user)
            return Response({'refresh':str(refresh), 'access':str(refresh.access_token), 'message':'Login successfully'},status=status.HTTP_200_OK)
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
        serializer = ProfileUpdateSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self, request):
        user = request.user
        serializer = ProfileUpdateSerializer(user,data=request.data, partial=True)
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
    
class ProjectView(APIView):
    permission_classes =[IsAdminUser] 
    
    def get(self,request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)\
        
    def post(self,request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        project = get_object_or_404(Project,pk=pk)
        serializer = ProjectSerializer(project,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request,pk):
        project = get_object_or_404(Project,pk=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class QuantitySheetView(APIView):
    # permission_classes = [IsAdminUser]        
    
    def get(self,request,project_id):
        quantity_sheets = QuantitySheet.objects.filter(project_id=project_id)
        serializer = QuantitySheetSerializer(quantity_sheets,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = QuantitySheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    # def put(self,request,pk):
    
class CostSheetView(APIView):
    def get(self,request,project_id):
        cost_sheets = CostSheet.objects.filter(project_id=project_id)
        serializer = CostSheetSerializer(cost_sheets,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,project_id):
        project = get_object_or_404(Project,id = project_id)
        quantity_sheets = QuantitySheet.objects.filter(project=project)
        
        total_cost = sum(sheet.value * 100 for sheet in quantity_sheets)
        
        cost_sheet =CostSheet.objects.create(project=project,total_cost=total_cost)
        serializer = CostSheetSerializer(cost_sheet)
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    