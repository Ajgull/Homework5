from email.policy import default
from random import choices

from django.db import models


# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(verbose_name="FirstName", max_length=255, blank=False)
    email = models.EmailField(unique=True, blank=False)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = "Customers"
        ordering = ['customer_name']

    def __str__(self):
        return self.customer_name


class Category(models.Model):
    category_name = models.CharField(max_length=255, verbose_name="Category Name")

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"
        ordering = ['category_name']

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_status  = [
        ('available', 'Available'),
        ('discontinued', 'Discontinued'),
        ('out_of_stock', 'Out of Stock'),
    ]
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(verbose_name="ProductName", max_length=255, blank=False)
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=30, choices=product_status, default='available')
    image = models.ImageField(upload_to="products/", verbose_name="Product Image", blank=True)
    categories = models.ManyToManyField(
        Category,
        blank=False,
        verbose_name="categories",
        related_name="product"
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Products"
        ordering = ['product_name']

    def __str__(self):
        return self.product_name

    def get_discount(self):
        return self.price * 0.9


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(verbose_name="Date of order", auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    customer = models.OneToOneField(
        Customer,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="customer",
        related_name="order"
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = "Orders"
        ordering = ['-order_id']

    def __str__(self):
        return f"Order {self.order_id} by {self.customer}"


class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="order",
        related_name="OrderDetail"
    )
    quantity = models.IntegerField(verbose_name="Quantity")
    product = models.ForeignKey(
        Product,
        blank=False,
        null=False,
        verbose_name="product",
        related_name="OrderDetail",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Order Detail'
        verbose_name_plural = "Order Details"
        ordering = ['product']

    def __str__(self):
        return f"{self.quantity} of {self.product.product_name} in Order {self.order.order_id}"


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    comment = models.TextField(verbose_name="Comment", blank=True)
    written_at = models.DateField(auto_now_add=True)
    product = models.ForeignKey(
        Product,
        blank=True,
        null=True,
        verbose_name="product",
        related_name="review",
        on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = "Reviews"
        ordering = ['written_at']

    def __str__(self):
        return f"Review {self.review_id} for {self.product.product_name}"
