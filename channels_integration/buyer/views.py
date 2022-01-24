from rest_framework import viewsets
from .serializers import BuyerSerializer
from .models import Buyer


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all().order_by('name')
    serializer_class = BuyerSerializer
