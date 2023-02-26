import indicators
import pandas as pd


#
# coins = indicators.fetch_coins_from_scalpstation_requests_html()
#
# print(coins)
#
# print(coins[1])
#
# print(indicators.get_market_data_error_handling('BTCUSDT','5m'))
# print(indicators.get_market_data_error_handling(coins[5],'5m'))
#
# for coin in coins:
#     print(indicators.get_market_data_error_handling(coin, '5m'))

data_f = indicators.get_all_info()
print(type(data_f))
print( data_f)