from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from orders.models import Order

class TestOrdersEnpoint(APITestCase):


    def test_get_orders(self):
        order1 = Order.objects.create(id='1234', marketplace='amazon', date='2014-10-21', amount=10, currency='EUR')
        order2 = Order.objects.create(id='56789', marketplace='amazon', date='2014-10-21', amount=50.5, currency='EUR')

        response = self.client.get('/orders/')

        self.assertEqual(response.status_code, 200)
        res = response.json()
        
        # Validate the response
        excepted = [
            {
                'id': order1.id,
                'marketplace': order1.marketplace,
                'date': order1.date,
                'amount':order1.amount,
                'currency': order1.currency,
            },
            {
                'id': order2.id,
                'marketplace': order2.marketplace,
                'date': order2.date,
                'amount':order2.amount,
                'currency': order2.currency,
            },
        ]
        self.assertEqual(excepted, response.json()['results'])


    def test_get_order_by_id(self):
        Order.objects.create(id='1234', marketplace='amazon', date='2014-10-21', amount=10, currency='EUR')
        order2 = Order.objects.create(id='56789', marketplace='amazon', date='2014-10-21', amount=50.5, currency='EUR')

        response = self.client.get("/orders/56789/")

        self.assertEqual(response.status_code, 200)
        excepted = {
                'id': order2.id,
                'marketplace': order2.marketplace,
                'date': order2.date,
                'amount':order2.amount,
                'currency': order2.currency,
            }
        
        self.assertEqual(excepted, response.json())


    def test_check_pagination(self):
        Order.objects.create(id='1234', marketplace='amazon', date='2014-10-21', amount=10, currency='EUR')
        Order.objects.create(id='56789', marketplace='amazon', date='2014-10-21', amount=50.5, currency='EUR')
        Order.objects.create(id='3', marketplace='amazon', date='2014-10-21', amount=10, currency='EUR')
        Order.objects.create(id='4', marketplace='amazon', date='2014-10-21', amount=50.5, currency='EUR')
        Order.objects.create(id='5', marketplace='amazon', date='2014-10-21', amount=10, currency='EUR')
        Order.objects.create(id='6', marketplace='amazon', date='2014-10-21', amount=50.5, currency='EUR')
        Order.objects.create(id='7', marketplace='amazon', date='2014-10-21', amount=10, currency='EUR')
        Order.objects.create(id='8', marketplace='amazon', date='2014-10-21', amount=50.5, currency='EUR')
        Order.objects.create(id='9', marketplace='amazon', date='2014-10-21', amount=10, currency='EUR')
        Order.objects.create(id='10', marketplace='amazon', date='2014-10-21', amount=50.5, currency='EUR')
        Order.objects.create(id='11', marketplace='amazon', date='2014-10-21', amount=10, currency='EUR')
        Order.objects.create(id='12', marketplace='amazon', date='2014-10-21', amount=50.5, currency='EUR')
        Order.objects.create(id='13', marketplace='amazon', date='2014-10-21', amount=10, currency='EUR')
        Order.objects.create(id='14', marketplace='amazon', date='2014-10-21', amount=50.5, currency='EUR')
        Order.objects.create(id='15', marketplace='amazon', date='2014-10-21', amount=10, currency='EUR')
        Order.objects.create(id='16', marketplace='amazon', date='2014-10-21', amount=50.5, currency='EUR')
        Order.objects.create(id='17', marketplace='amazon', date='2014-10-21', amount=10, currency='EUR')
        Order.objects.create(id='18', marketplace='amazon', date='2014-10-21', amount=50.5, currency='EUR')
        Order.objects.create(id='19', marketplace='amazon', date='2014-10-21', amount=10, currency='EUR')
        Order.objects.create(id='20', marketplace='amazon', date='2014-10-21', amount=50.5, currency='EUR')
        Order.objects.create(id='21', marketplace='amazon', date='2014-10-21', amount=10, currency='EUR')

        response = self.client.get('/orders/?page=2')

        self.assertEqual(response.status_code, 200)
        res = response.json()

        # validate pagination
        self.assertEqual(21, res['count'])
        self.assertEqual('http://testserver/orders/?page=3', res['next'])
        self.assertEqual('http://testserver/orders/', res['previous'])