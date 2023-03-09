from django.db import models


class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
