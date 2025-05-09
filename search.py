import pandas as pd

from data import get_data
from main import COST, INSTRUMENTS


def start(date_start):
    data = get_data(date_start)
    cost_series = pd.Series(COST)
    cost_series.index = INSTRUMENTS

    prices_usd = round(data * cost_series, 2)
    exact_price = prices_usd[prices_usd.nunique(axis=1) == 1]

    if not exact_price.empty:
        print(f'Found a date where all usd prices match: ...')
    else:
        data = get_data(date_start, test=True)
        prices_usd = round(data * cost_series, 2)
        exact_price = prices_usd[prices_usd.nunique(axis=1) == 1]