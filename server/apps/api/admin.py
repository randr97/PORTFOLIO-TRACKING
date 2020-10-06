from django.contrib import admin

from apps.api.models import Trade


class TradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticker', 'price', 'shares', 'trade_type')
    search_fields = ('ticker', 'shares')


admin.site.register(Trade, TradeAdmin)
