import tkinter as tk
import typing

from interface.styling import *

from connectors.binance import BinanceFuturesClient
from connectors.bitmex import BitmexClient

class StrategyEditor(tk.Frame):
     def __init__(self, root, binance: BinanceFuturesClient, bitmex: BitmexClient, *args, **kwargs):
        super().__init__(*args, **kwargs)