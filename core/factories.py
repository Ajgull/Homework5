import factory

from factory.django import ImageField

from core.models import Customer, Product, Category, Order, OrderDetail, Review


class CustomerFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    email = factory.Faker('email')

    class Meta:
        model = Customer


class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    price = factory.Faker('random_int', min=10, max=100000)
    status = factory.Faker('random_element', elements=['available', 'discontinued', 'out_of_stock'])
    image = ImageField()

    class Meta:
        model = Product


class OrderFactory(factory.django.DjangoModelFactory):
    customer = factory.SubFactory(CustomerFactory)

    class Meta:
        model = Order


class OrderDetailFactory(factory.django.DjangoModelFactory):
    order = factory.SubFactory(OrderFactory)
    quantity = factory.Faker('random_int', min=1, max=10)
    product = factory.SubFactory(ProductFactory)

    class Meta:
        model = OrderDetail


class ReviewFactory(factory.django.DjangoModelFactory):
    comment = factory.Faker('sentence')
    product = factory.SubFactory(ProductFactory)
    customer = factory.SubFactory(CustomerFactory)
    written_at = factory.Faker('date')

    class Meta:
        model = Review
