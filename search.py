import pandas as pd

from data import get_data
from main import COST, INSTRUMENTS


def start(date_start):
    data = get_data(date_start)
    cost_series = pd.Series(COST)
    cost_series.index = INSTRUMENTS
    prices_usd = data[INSTRUMENTS] * cost_series