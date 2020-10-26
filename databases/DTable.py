import pandas as pd
import numpy as np
import matplotlib as plt
import yfinance as yf


def get(ticker) -> dict:
    stock = yf.Ticker(ticker)
    pass


def add(new_ticker, new_tags):
    pass


def remove(old_ticker):

    pass


def replace(old_ticker, new_ticker, new_tags):
    pass


def modify(old_ticker: str, new_tags: list):
    pass


def get_tags(old_ticker):
    pass
