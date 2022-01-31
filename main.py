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
    bitmex = BitmexClient(TEST_BITMAX_ID, TEST_BITMAX_SECRET, True)

    root = Root(binance, bitmex)
    root.mainloop()