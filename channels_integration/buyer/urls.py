from django.urls import include, path
from rest_framework import routers
from .views import BuyerViewSet

router = routers.DefaultRouter()
router.register(r'buyers', BuyerViewSet, basename="buyers")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
