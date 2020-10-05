from django.urls import path
from apps.api import views


urlpatterns = [
    # Trade APIs
    path(r'list_trades/', views.TradeView.as_view(actions={
        'get': 'list',
    }), name='list_trade'),
    path(r'create_trade/', views.TradeView.as_view(actions={
        'post': 'create_trade',
    }), name='create_trade'),
    path(r'update_trade/', views.TradeView.as_view(actions={
        'put': 'update_trade',
    }), name='update_trade'),
    path(r'delete_trade/<int:pk>/', views.TradeView.as_view(actions={
        'delete': 'delete_trade',
    }), name='delete_trade'),
    # portfolio APIs
    path(r'fetch_portfolio/', views.TradeView.as_view(actions={
        'get': 'fetch_portfolio',
    }), name='fetch_portfolio'),
    path(r'fetch_returns/', views.TradeView.as_view(actions={
        'get': 'fetch_returns',
    }), name='fetch_returns'),
]
