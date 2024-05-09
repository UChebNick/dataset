import okx.MarketData as MarketData

flag = "1"  # Production trading:0 , demo trading:1
marketDataAPI = MarketData.MarketAPI(flag=flag)

# Retrieve historical candlestick data for BTC-USDT with 1-hour bars



def get_arr():

    result = marketDataAPI.get_history_candlesticks(
        instId="TON-USDT",
        bar="1m"

    )
    ans = []
    for i in result['data'][:-1]:
        ans.append(float(i[3]))

    return list(reversed(ans))

print(get_arr())