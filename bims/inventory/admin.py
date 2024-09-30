from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomUser),
admin.site.register(CostSheet),
admin.site.register(Project),
admin.site.register(SubCategory),
admin.site.register(Category),
admin.site.register(QuantitySheet),
admin.site.register(InventoryItem)