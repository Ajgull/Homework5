from django.contrib import admin

from core import models


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
    )


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'order',
        'quantity',
    )


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'status',
    )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'id',
        'created_at',
        'updated_at',
    )


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'product',
        'comment',
        'written_at',
    )
