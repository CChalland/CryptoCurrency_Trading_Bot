import tkinter as tk
import logging

from connectors.bitmex import BitmexClient
from connectors.binance import BinanceFuturesClient

from interface.styling import *
# from interface.logging_component import Logging
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
