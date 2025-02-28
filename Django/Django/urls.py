from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from orders.views import OrderViewset


router = routers.SimpleRouter()
router.register('orders', OrderViewset, basename='orders')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
