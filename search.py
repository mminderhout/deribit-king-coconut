import pandas as pd

from data import get_data
from main import COST, INSTRUMENTS


def start(date_start, date_end):
    best_matches = {}
    for test in [False, True]:
        data = get_data(date_start, date_end, test=test)
        cost_series = pd.Series(COST)
        cost_series.index = INSTRUMENTS

        prices_usd = round(data * cost_series, 2)
        prices_usd['ssd'] = ((prices_usd.sub(prices_usd.mean(axis=1), axis=0)) ** 2).sum(axis=1)
        best_match = prices_usd.nsmallest(1, "ssd")
        best_matches['prod' if not test else 'test'] = best_match

    def print_output(env):
        price = pd.DataFrame(best_matches[env][INSTRUMENTS]).median(axis=1)
        time = price.index[0].strftime('%Y-%m-%d %H:%M:%S')
        ssd = best_matches[env]['ssd'].iloc[0]
        missing = best_matches[env][INSTRUMENTS].isna().sum(axis=1).iloc[0]
        print(f'The best match occurs on {time}, at a price of {price.iloc[0]} in the {env} environment.\n'
              f'The sum of squared differences from the mean price at this time is {round(ssd, 6)}, and there are '
              f'{missing} missing products.')

    if best_matches['prod']['ssd'].values < best_matches['test']['ssd'].values:
        print_output('prod')
    elif best_matches['prod']['ssd'].values > best_matches['test']['ssd'].values:
        print_output('test')

