from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import ChannelsViewSet


router = routers.DefaultRouter()
router.register(r'channels', ChannelsViewSet, basename='channels')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'
    ))
]
