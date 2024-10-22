from django.test import TestCase
from django.urls import reverse

from core import factories, models


class ProductShelfTestCase(TestCase):

    def setUp(self) -> None:
        self.product = factories.ProductFactory()

    def test_get_product_shelf_list(self) -> None:
        url = reverse('produce_shelf')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['produces'].count(), models.Product.objects.count())
        # print(response.context['produces'].count(), models.Product.objects.count())

    def test_get_product_detail(self) -> None:
        url = reverse('produce_detail', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_product(self) -> None:
        url = reverse('produce_update', kwargs={'pk': self.product.pk})
        old_name = self.product.name
        old_price = self.product.price
        res = {
            'name': 'new_name',
            'price': old_price
        }
        response = self.client.post(url, res)
        self.product.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(self.product.name, old_name)

    def test_delete_product(self) -> None:
        url = reverse('produce_delete', kwargs={'pk': self.product.pk})
        old_prod_count = models.Product.objects.count()

        response = self.client.delete(url)

        self.assertEqual(response.status_code, 302)
        self.assertGreater(old_prod_count, models.Product.objects.count())
        print(old_prod_count, models.Product.objects.count())

    def test_create_product(self) -> None:
        url = reverse('produce_create')
        old_prod_count = models.Product.objects.count()

        res = {
            'name': 'new_name',
            'price': 100,
            'status': 'available',
            'image': 'media/products/вода.png'
        }

        response = self.client.post(url, res)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(old_prod_count + 1, models.Product.objects.count())
        self.assertGreater(models.Product.objects.count(), old_prod_count)
