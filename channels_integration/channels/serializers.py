from rest_framework import serializers
from .models import Channels


class ChannelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channels
        fields = '__all__'
