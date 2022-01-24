from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from .channels.views import ChannelsViewSet
from .buyer.views import BuyerViewSet


router = routers.DefaultRouter()
router.register(r'channels', ChannelsViewSet, basename='channels')
router.register(r'buyers', BuyerViewSet, basename='buyers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'
    )),
]
