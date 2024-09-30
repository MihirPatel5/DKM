from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from .models import Project,QuantitySheet,CostSheet,Category,SubCategory
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'first_name', 'last_name', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        password = get_random_string(8)
        user.set_password(password)
        user.save()
        send_mail(
            subject="Your Login Credentials",
            message=f"Your account has been created.\nUsername: {user.username}\nPassword: {password}",
            from_email="gam.globaliasoft@gmail.com",
            recipient_list=[user.email],
        )

        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ['id','email','phonenumber','first_name','last_name','is_active']
        

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['username','email','phone_number','first_name','last_name']
        
class PasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True,validators=[validate_password])
    
    def validate(self,attrs):
        user = self.context['request'].user
        if not user.check_password(attrs['old_password']):
            raise serializers.ValidationError({'old_password':'old password is Invalid, Please enter the correct one.'})
        return attrs
    
    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model =Project
        fields = ['id','name','description','user','creatd_at']
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields = ['id','name']
        
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id','name','category']
        
class QuantitySheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantitySheet
        fields = ['id','project','sub_category','value']
        
class CostSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostSheet
        fields = ['id','project','total_cost','created_at']        