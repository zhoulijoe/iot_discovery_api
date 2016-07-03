from django.conf.urls import url, include
from rest_framework import routers

from products.views import ProductViewSet

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet, base_name='product')

urlpatterns = [
    url(r'^', include(router.urls)),
]
