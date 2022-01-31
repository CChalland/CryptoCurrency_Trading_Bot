import tkinter as tk
import logging
import time

from connectors.bitmex import BitmexClient
from connectors.binance import BinanceFuturesClient

from interface.styling import *
from interface.logging_component import Logging
# from interface.watchlist_component import Watchlist
# from interface.trades_component import TradesWatch
# from interface.strategy_component import StrategyEditor


logger = logging.getLogger()


class Root(tk.Tk):
    def __init__(self, binance: BinanceFuturesClient, bitmex: BitmexClient):
        super().__init__()

        self.binance = binance
        self.bitmex = bitmex

        self.title("Trading Bot")
        self.configure(bg=BG_COLOR)

        self._left_frame = tk.Frame(self, bg=BG_COLOR)
        self._left_frame.pack(side=tk.LEFT)
        
        self._right_frame = tk.Frame(self, bg=BG_COLOR)
        self._right_frame.pack(side=tk.LEFT)
        
        self._logging_frame = Logging(self._left_frame, bg=BG_COLOR)
        self._logging_frame.pack(side=tk.TOP)
        
        self._logging_frame.add_log("This is a text message")
        time.sleep(2)
        self._logging_frame.add_log("second message")