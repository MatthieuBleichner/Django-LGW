from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from orders.models import Order

class TestOrdersEnpoint(APITestCase):


    def test_get_orders(self):
        order1 = Order.objects.create(ref_id='1234', marketplace='amazon', date='2014-10-21', amount=10, currency='EUR')
        order2 = Order.objects.create(ref_id='56789', marketplace='amazon', date='2014-10-21', amount=50.5, currency='EUR')

        response = self.client.get('/api/orders/')

        self.assertEqual(response.status_code, 200)
        excepted = [
            {
                'ref_id': order1.ref_id,
                'marketplace': order1.marketplace,
                'date': order1.date,
                'amount':order1.amount,
                'currency': order1.currency,
            },
            {
                'ref_id': order2.ref_id,
                'marketplace': order2.marketplace,
                'date': order2.date,
                'amount':order2.amount,
                'currency': order2.currency,
            },
        ]
        self.assertEqual(excepted, response.json())

    def test_get_order_by_id(self):
        order1 = Order.objects.create(ref_id='1234', marketplace='amazon', date='2014-10-21', amount=10, currency='EUR')
        order2 = Order.objects.create(ref_id='56789', marketplace='amazon', date='2014-10-21', amount=50.5, currency='EUR')

        response = self.client.get("/api/orders/56789/")

        self.assertEqual(response.status_code, 200)
        excepted = {
                'ref_id': order2.ref_id,
                'marketplace': order2.marketplace,
                'date': order2.date,
                'amount':order2.amount,
                'currency': order2.currency,
            }
        
        self.assertEqual(excepted, response.json())


