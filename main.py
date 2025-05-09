import requests
from datetime import datetime

import search

COST = {
    'ETH': 0.0013371,
    'BTC': 0.00005181,
    'PAX': 0.0015856,
    'SOL': 0.020196,
    'XRP': 7.2942,
    'ADA': 7.3376
}
INSTRUMENTS = [
    'BTC-PERPETUAL',
    'ETH-PERPETUAL',
    'PAXG_USDC-PERPETUAL',
    'SOL_USDC-PERPETUAL',
    'XRP_USDC-PERPETUAL',
    'ADA_USDC-PERPETUAL'
]


def find_start_date():
    url = "https://www.deribit.com/api/v2/public/get_instrument"
    creation_timestamps = []
    for instrument in INSTRUMENTS:
        params = {"instrument_name": instrument}
        response = requests.get(url, params=params)
        creation_timestamps.append(response.json()['result']['creation_timestamp'])
    print(f'The earliest all products were available is {datetime.fromtimestamp(max(creation_timestamps) / 1000).strftime('%Y-%m-%d %H:%M:%S')}.')
    return max(creation_timestamps) / 1000


def main():
    date_start = find_start_date()
    search.start(date_start)


if __name__ == "__main__":
    main()