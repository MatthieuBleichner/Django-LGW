from io import StringIO
from django.core.management import call_command
from django.test import TestCase
import os
from orders.models import Order, Address

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

class ImportDataTest(TestCase):
    def test_command_basic_output(self):
        out = StringIO()
        call_command("importData", os.path.join(THIS_DIR, 'orders-test.xml'), stdout=out)
        self.assertIn('Successfully import 5 orders', out.getvalue())


    def test_command_output_with_no_file(self):
        out = StringIO()
        call_command("importData", os.path.join(THIS_DIR, 'unExistingFile.xml'), stdout=out)
        self.assertIn('does not exist', out.getvalue())

    
    def test_command_output_with_wrong_file_format(self):
        out = StringIO()
        call_command("importData", os.path.join(THIS_DIR, 'file.pdf'), stdout=out)
        self.assertIn('wrong file format. Please use an xml file', out.getvalue())

    def test_command_successfully_feed_database(self):
        out = StringIO()
        call_command("importData", os.path.join(THIS_DIR, 'orders-test.xml'), stdout=out)

        self.assertEqual(Order.objects.count(), 5)
        self.assertEqual(Order.objects.all()[0].marketplace, 'amazon')
        self.assertEqual(Order.objects.all()[0].id, '111-2222222-3333333')
        self.assertEqual(Order.objects.all()[0].date.strftime('%Y-%m-%d'), '2014-10-21')
        self.assertEqual(Order.objects.all()[0].amount, 34.5)
        self.assertEqual(Order.objects.all()[0].currency, 'EUR')
        self.assertEqual(Order.objects.all()[0].billing_adress.id, 1)

        self.assertEqual(Address.objects.count(), 5)
        self.assertEqual(Address.objects.all()[0].address, '014 rue de la poupée')
        self.assertEqual(Address.objects.all()[0].zipCode, '75000')
        self.assertEqual(Address.objects.all()[0].city, 'Paris')
        self.assertEqual(Address.objects.all()[0].email, 'web1n0r@marketplace.amazon.fr')


    def test_command_with_missing_data(self):
        out = StringIO()
        call_command("importData", os.path.join(THIS_DIR, 'orders-test-with-missing-data.xml'), stdout=out)
        self.assertEqual(Order.objects.count(), 1)

    def test_command_with_missing_tags(self):
        out = StringIO()
        call_command("importData", os.path.join(THIS_DIR, 'orders-test-with-missing-tags.xml'), stdout=out)
        self.assertEqual(Order.objects.count(), 1)