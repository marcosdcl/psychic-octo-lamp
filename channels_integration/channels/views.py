from rest_framework import viewsets
from .models import Channels
from .serializers import ChannelsSerializer


class ChannelsViewSet(viewsets.ModelViewSet):
    queryset = Channels.objects.all().order_by('id')
    serializer_class = ChannelsSerializer
