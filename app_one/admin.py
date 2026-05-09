from django.contrib import admin
from .models import Category, Product, User, Cart, Transaction


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'first_name', 'last_name', 'is_active']
    list_display_links = ['phone_number']




# admin.site.register(CustomUser)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_stock', 'category']
    list_display_links = ['name']



@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'product', 'count', 'created']
    list_display_links = ['user']



@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'product_name' ,'amount', 'created']
    list_display_links = ['user']



 # def get_product_price(self, obj):
 #        return obj.product_name.price
 #
 #    get_product_price.short_description = "Mahsulot narxi"