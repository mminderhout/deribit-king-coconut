import requests

import search


COST = {
    'BTC': 0.00005181,
    'ETH': 0.0013371,
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
    second_highest = sorted(set(creation_timestamps), reverse=True)[1]
    return second_highest / 1000


def main():
    date_start = find_start_date()
    search.start(date_start, None)


if __name__ == "__main__":
    main()