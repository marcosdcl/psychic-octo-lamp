from django.db import models


class Channels(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True)
    contact = models.CharField(max_length=100, null=False, blank=False)
    url = models.CharField(max_length=100, null=False, blank=False)
    rate = models.FloatField(null=False)

    def __str__(self):
        return f'channel {self.name}'
