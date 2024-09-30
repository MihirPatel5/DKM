from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="subcategories")
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class QuantitySheet(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="quanity_sheets")
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.project.name} - {self.sub_category.name}"
    
    
class CostSheet(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="coast_sheets")
    total_cost = models.DecimalField(max_digits=12,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.project.name} - Cost Sheet"
    
    