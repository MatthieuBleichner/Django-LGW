from django.core.management.base import BaseCommand, CommandError
from xml.dom import minidom
from orders.models import Order, Address
from django.core.exceptions import ValidationError


class Command(BaseCommand):
    help = "Import orders from an xml file"

    def add_arguments(self, parser):
        parser.add_argument("xmlFile", nargs="+", type=str)

    
    def __getValue(self, rootNode, name, defaultValue):
        element = rootNode.getElementsByTagName(name)
        if element:
            node = element[0].firstChild
            return node.nodeValue if node else defaultValue
        return defaultValue

    def handle(self, *args, **options):
        xmlFile = options["xmlFile"][0]

        # Check if the file extension is xml
        if xmlFile.lower().endswith('.xml') == False:
            self.stdout.write(
                self.style.ERROR('wrong file format. Please use an xml file')
            )
            return

        # Check if file exists
        try:
            xmldoc = minidom.parse(xmlFile)
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR('File "%s" does not exist' % xmlFile)
            )
            return
        
        # Retrieve all orders elements
        orders = xmldoc.getElementsByTagName('order')
        imported_orders = 0

        # Parse all orders and save them to the database
        for xmlOrder in orders:
            order = Order()

            order.marketplace = self.__getValue(xmlOrder, 'marketplace', '')
            order.amount = self.__getValue(xmlOrder, 'order_amount', 0)
            order.currency = self.__getValue(xmlOrder, 'order_currency', '')

            id_value = self.__getValue(xmlOrder, 'order_id', '') #keep value for logging purposes
            order.id = id_value
            
            date_value = self.__getValue(xmlOrder, 'order_purchase_date', '')
            if (date_value != ''): # NOTE: 02.28.2025 specific for date format. If it's not a valid date do not set it, keep model default behaviour for null values
                order.date = date_value
            

            # Retrieve billing address
            address_node = xmlOrder.getElementsByTagName('billing_address')
            if address_node:
                billing_address, created = Address.objects.get_or_create(
                        email=self.__getValue(address_node[0], 'billing_email', ''))
                if not created:
                    order.billing_adress = billing_address
                else:
                    billing_address.address = self.__getValue(address_node[0], 'billing_address', '')
                    billing_address.zipCode = self.__getValue(address_node[0], 'billing_zipcode', '')
                    billing_address.city = self.__getValue(address_node[0], 'billing_city', '')
                    billing_address.email = self.__getValue(address_node[0], 'billing_email', '')
                    
                    try: 
                        billing_address.save()
                    except:
                        pass
                    else:
                        order.billing_adress = billing_address
            self.stdout.write(
                'Importing order with id: "%s" ... ' %  id_value, ending=""
            )
            try: 
                order.save()
            except ValidationError as e:
                self.stdout.write(
                    self.style.ERROR('NOK %s' % e)
                )
                continue 

            imported_orders += 1
            self.stdout.write(
                self.style.SUCCESS('OK')
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully import %d orders from "%s"' % ( imported_orders, options["xmlFile"][0]))
        )