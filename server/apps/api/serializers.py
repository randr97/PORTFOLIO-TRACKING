from django.db.models import Sum
from rest_framework import serializers

from apps.api.models import Trade
from apps.api.enum import TradeType


class TradeSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=False, required=False)

    class Meta:
        model = Trade
        fields = ['id', 'ticker', 'price', 'shares', 'trade_type']

    def validate(self, data):
        """
        This method is by default called by DRF before create or update
        It ensures that trade does not become negative
        """
        exclude_list = []
        if data.get('id'):
            # This is during update we need to exclude the id from out agg query
            exclude_list.append(data['id'])
        total_shares_present = Trade.objects.filter(
            ticker=data['ticker']).exclude(pk__in=exclude_list).aggregate(Sum('shares'))['shares__sum'] or 0
        if TradeType[data['trade_type']].value == TradeType.SELL.value:
            data['shares'] = 0 - data['shares']

        total_shares_post = total_shares_present + data['shares']

        if total_shares_post < 0:
            raise serializers.ValidationError("This trade is invalid. Total number of shares cannot be negative")
        return data

    def create(self, data):
        return Trade.objects.create(**data)

    def update(self, trade_object, data):
        trade_object.__dict__.update(data)
        trade_object.save()
        return trade_object

    def to_representation(self, data):

        return_data = {
            'id': data.id,
            'ticker': data.ticker,
            'price': data.price,
            'shares': data.shares,
            'trade_type': data.trade_type,
        }

        if TradeType[return_data['trade_type']].value == TradeType.SELL.value:
            return_data['shares'] = 0 - return_data['shares']
        return return_data
