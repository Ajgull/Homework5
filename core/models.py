from django.db import models

from core import consts


# Create your models here.
class Customer(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255, blank=False)
    email = models.EmailField(unique=True, blank=False)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name of Category')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='ProductName', max_length=255, blank=False)
    price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=30, choices=consts.PRODUCT_STATUS, default='available')
    image = models.ImageField(upload_to='products/', verbose_name='Product Image', blank=True)
    categories = models.ManyToManyField(Category, blank=False, verbose_name='categories', related_name='product')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name

    def get_discount(self) -> str:
        return self.price * 0.9


class Order(models.Model):
    created_at = models.DateField(verbose_name='Date of order', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(
        Customer, blank=False, null=False, on_delete=models.CASCADE, verbose_name='customer', related_name='orders'
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'Order {self.id} by {self.customer}'


class OrderDetail(models.Model):
    order = models.OneToOneField(
        Order, blank=False, null=False, on_delete=models.CASCADE, verbose_name='order', related_name='details'
    )
    quantity = models.PositiveIntegerField(verbose_name='Quantity')
    product = models.ForeignKey(
        Product, blank=False, null=False, verbose_name='product', related_name='details', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Order Detail'
        verbose_name_plural = 'Order Details'
        ordering = ['product']

    def __str__(self) -> str:
        return f'{self.quantity} of {self.product.name} in Order {self.order.id}'


class Review(models.Model):
    comment = models.TextField(verbose_name='Comment', blank=False)
    written_at = models.DateField(auto_now_add=True)
    product = models.ForeignKey(
        Product, blank=True, null=True, verbose_name='product', related_name='reviews', on_delete=models.CASCADE
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['written_at']

    def __str__(self) -> str:
        return f'Review {self.id} for {self.product.name}'
