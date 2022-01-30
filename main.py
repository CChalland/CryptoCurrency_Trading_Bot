from decouple import config
import tkinter as tk
import logging
from connectors.binance import BinanceFuturesClient
from connectors.bitmex import BitmexClient
from interface.root_component import Root
# testnet.binancefuture.com API keys
TEST_BINANCE_KEY = config('TEST_BINANCE_KEY')
TEST_BINANCE_SECRET = config('TEST_BINANCE_SECRET')
# testnet.bitmex.com API keys
TEST_BITMAX_ID = config('TEST_BITMAX_ID')
TEST_BITMAX_SECRET = config('TEST_BITMAX_SECRET')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':
    binance = BinanceFuturesClient(TEST_BINANCE_KEY, TEST_BINANCE_SECRET, True)
    # print(binance.get_contracts())
    # print(binance.get_bid_ask("BTCUSDT"))
    # print(binance.get_historical_candles("BTCUSDT", "1h"))
    # print(binance.get_balances())
    # print(binance.place_order("BTCUSDT", "BUY", 0.01, "LIMIT", 20000, "GTC"))
    # print(binance.get_order_status("BTCUSDT", 2712672670))
    # print(binance.cancel_order("BTCUSDT", 2712672670))
    bitmex = BitmexClient(TEST_BITMAX_ID, TEST_BITMAX_SECRET, True)
    # print(bitmex.place_order(bitmex.contracts['XBTUSD'], "Limit", 120.4, "Buy", 20000.4939338, "GoodTillCancel"))

    root = Root(binance, bitmex)
    root.mainloop()