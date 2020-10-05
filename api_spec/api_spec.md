<!-- http://localhost:9090/api/list_trades/ -->
# This API lists all the securities and the corresponding trades
## http://localhost:9090/api/list_trades/

## response
```
{
    "ok": true,
    "data": [
        {
            "ticker": "TCS",
            "trades": [
                {
                    "id": 7,
                    "ticker": "TCS",
                    "price": 50.0,
                    "shares": 10,
                    "trade_type": "BUY"
                },
                {
                    "id": 8,
                    "ticker": "TCS",
                    "price": 50.0,
                    "shares": 30,
                    "trade_type": "BUY"
                },
                {
                    "id": 10,
                    "ticker": "TCS",
                    "price": 50.0,
                    "shares": 10,
                    "trade_type": "SELL"
                }
            ]
        },
        {
            "ticker": "INFY",
            "trades": [
                {
                    "id": 11,
                    "ticker": "INFY",
                    "price": 50.0,
                    "shares": 10,
                    "trade_type": "BUY"
                },
                {
                    "id": 12,
                    "ticker": "INFY",
                    "price": 50.0,
                    "shares": 20,
                    "trade_type": "BUY"
                },
                {
                    "id": 13,
                    "ticker": "INFY",
                    "price": 50.0,
                    "shares": 30,
                    "trade_type": "BUY"
                },
                {
                    "id": 14,
                    "ticker": "INFY",
                    "price": 40.0,
                    "shares": 10,
                    "trade_type": "SELL"
                }
            ]
        }
    ]
}
```
<!-- http://localhost:9090/api/create_trade/ -->
# This API allows you to insert a trade of type BUY or SELL
## http://localhost:9090/api/create_trade/

## request body
```
{
    "ticker": "TCS",
    "price": 50,
    "shares": 10,
    "trade_type": "BUY"
}
```
> Note: If you sell, there is a validation to prevent your total number of share from becoming negative

<!-- http://localhost:9090/api/update_trade/ -->
# This API allows you to update a trade that has already been inserted
## http://localhost:9090/api/update_trade/

## request body
```
{
    "id": 1,
    "ticker": "TCS",
    "price": 50.0,
    "shares": 10,
    "trade_type": "BUY"
}
```
> Note: If you update trade type from BUY to  SELL, there is a validation to prevent your total number of share from becoming negative

<!-- http://localhost:9090/api/delete_trade/<int:pk>/ -->
# This API allows you to delete a trade that has already been inserted
## http://localhost:9090/api/delete_trade/<int:pk>/

## pk is the id of the trade to be deleted
> Note: If you delete trade type BUY, there is a validation to prevent your total number of share from becoming negative

<!-- http://localhost:9090/api/fetch_portfolio/ -->
# This API returns the entire portfolio with avg_buy_price
## http://localhost:9090/api/fetch_portfolio/

## response
```
[
    {
        "ticker": "INFY",
        "average_buy_price": 50.0,
        "total_shares": 50
    },
    {
        "ticker": "TCS",
        "average_buy_price": 50.0,
        "total_shares": 30
    }
]
```

<!-- http://localhost:9090/api/fetch_returns/ -->
# This API gives the returns of the portfolio
## http://localhost:9090/api/fetch_returns/

## response
```
{
    "portfolio_returns": 4000.0
}
```
