from rest_framework.serializers import ModelSerializer
 
from orders.models import Order, Address
 

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['address', 'zipCode', 'city', 'email']

class OrderSerializer(ModelSerializer):
    billing_adress = AddressSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'marketplace', 'date', 'amount', 'currency', 'billing_adress']
