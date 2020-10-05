from django.db import models
from apps.api.enum import TradeType


class Trade(models.Model):
    """
    This Model represents the trades that are made of type buy/sell
    """
    id = models.AutoField(primary_key=True)
    ticker = models.CharField(max_length=255, blank=False, null=False)
    price = models.FloatField()
    shares = models.IntegerField()
    trade_type = models.CharField(max_length=255, choices=TradeType.choices())

    REQUIRED_FIELDS = ['id', 'ticker', 'price', 'shares', 'type']
