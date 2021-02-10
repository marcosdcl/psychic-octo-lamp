from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('channels_integration.channels.urls')),
    path('', include('channels_integration.buyer.urls')),
]
