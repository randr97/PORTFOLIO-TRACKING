from django.db.models import Sum, F, FloatField, IntegerField
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import generics, views
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from apps.api.models import Trade
from apps.api.enum import TradeType
from apps.api.serializers import TradeSerializer


class TradeView(ViewSet):
    """
    This view is according to the question asked in the problem statement
    """

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Trade.objects.all()
        serializer_context = {
            'request': request,
        }
        serialized_data = TradeSerializer(
            queryset, many=True, context=serializer_context
        ).data
        response = {}

        for each_trade in serialized_data:
            if response.get(each_trade['ticker']):
                response[each_trade['ticker']]['trades'].append(each_trade)
            else:
                response[each_trade['ticker']] = {
                    'ticker': each_trade['ticker'],
                    'trades': [each_trade],
                }

        return_data = {
            'ok': True,
            'data': response.values(),
        }
        return Response(return_data)

    def create_trade(self, request):
        """
        Request body structure
        body = {
            "ticker": "TCS",
            "price": 50,
            "shares": 10,
            "trade_type": "BUY"
        }
        """
        trade_serializer = TradeSerializer(data=request.data)
        if trade_serializer.is_valid():
            trade_serializer.save()
            return Response(trade_serializer.data, status=status.HTTP_201_CREATED)
        return Response(trade_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update_trade(self, request):
        """
        Request body structure
        ID has to be passed via body
        body = {
            "id": 1,
            "ticker": "TCS",
            "price": 50,
            "shares": 10,
            "trade_type": "BUY"
        }
        """
        trade_object = get_object_or_404(Trade, pk=request.data['id'])
        trade_serializer = TradeSerializer(trade_object, data=request.data)
        if trade_serializer.is_valid():
            trade_serializer.save()
            return Response(trade_serializer.data)
        return Response(trade_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_trade(self, request, pk):
        trade_object = get_object_or_404(Trade, pk=pk)
        total_shares_present = Trade.objects.filter(
            ticker=trade_object.ticker).exclude(pk__in=[pk]).aggregate(Sum('shares'))['shares__sum'] or 0
        if total_shares_present < 0:
            return Response(
                "Cannot delete trade. Total trades for this ticker cannot be negative",
                status=status.HTTP_400_BAD_REQUEST
            )
        response = TradeSerializer(trade_object).data
        trade_object.delete()
        return Response(response)

    def fetch_portfolio_data(self):
        trade_objects = Trade.objects.filter(
            trade_type=TradeType.BUY.value
        ).values('ticker').annotate(
            average_buy_price=Sum(F('price') * F('shares'), output_field=FloatField()) / Sum(F('shares'), output_field=FloatField()) # noqa
        )
        ticker_dict = {x['ticker']: x for x in trade_objects}
        ticker_shares = Trade.objects.values('ticker').annotate(total_shares=Sum(F('shares')))
        for each_ticker in ticker_shares:
            ticker_dict[each_ticker['ticker']].update({
                'total_shares': each_ticker['total_shares']
            })
        response = ticker_dict.values()
        return response

    def fetch_portfolio(self, request):
        response = self.fetch_portfolio_data()
        return Response(response)

    def fetch_returns(self, request):
        CURRENT_PRICE_OF_SECURITY = 100
        response = self.fetch_portfolio_data()
        result = 0
        for each_ticker in response:
            result += (CURRENT_PRICE_OF_SECURITY - each_ticker['average_buy_price']) * each_ticker['total_shares']
        return Response({
            'portfolio_returns': result,
        })
