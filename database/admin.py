from django.contrib import admin
from database import models


# Register your models here.

@admin.register(models.Customer)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_id',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

@admin.register(models.OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('product','order','quantity',)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'status')


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_id', 'order_date')


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'comment', 'written_at',)
