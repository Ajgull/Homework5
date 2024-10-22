from django.test import TestCase
from django.urls import reverse
from core import factories, models


class ProductShelfTestCase(TestCase):

    def setUp(self) -> None:
        self.product = factories.ProductFactory()

    def test_get_product_shelf(self) -> None:
        url = reverse('produce_shelf')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['produces'].count(), models.Product.objects.count())
        print(response.context['produces'].count(), models.Product.objects.count())

    # def test_get_product_detail(self) -> None:
    #     url = reverse('produce_detail', kwargs={'pk': self.product.pk})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
