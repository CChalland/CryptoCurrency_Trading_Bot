from decouple import config
import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root

# testnet.binancefuture.com API keys
TEST_BINANCE_KEY = config('TEST_BINANCE_KEY')
TEST_BINANCE_SECRET = config('TEST_BINANCE_SECRET')
# testnet.bitmex.com API keys
TEST_BITMAX_ID = config('TEST_BITMAX_ID')
TEST_BITMAX_SECRET = config('TEST_BITMAX_SECRET')

# Create and configure the logger object
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient(TEST_BINANCE_KEY,
                            TEST_BINANCE_SECRET,
                            testnet=True, futures=True)
    bitmex = BitmexClient(TEST_BITMAX_ID, TEST_BITMAX_SECRET, testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
