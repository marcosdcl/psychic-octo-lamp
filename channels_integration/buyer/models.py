from django.db import models
from channels_integration.channels.models import Channels


class Buyer(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=50, null=False)
    zip_code = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    channel = models.ForeignKey(Channels, on_delete=models.CASCADE)

    def __str__(self):
        return f"Buyer {self.name}"
