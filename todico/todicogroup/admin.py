from django.contrib import admin
from .models import Category, Product
# Register your models here.
class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title','price', 'category','date_added','description')

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategorie)