from rest_framework.viewsets import ReadOnlyModelViewSet
from orders.models import Order
from orders.serializers import OrderSerializer
class OrderViewset(ReadOnlyModelViewSet):

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()