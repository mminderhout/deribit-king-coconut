import time

import requests
from datetime import datetime, timedelta
import pandas as pd

from main import INSTRUMENTS


def get_data(start, end = None, test=False):
    url = "https://www.deribit.com/api/v2/public/get_tradingview_chart_data"
    if test:
        url = "https://test.deribit.com/api/v2/public/get_tradingview_chart_data"
    if end is None:
        end = time.time()

    dataframes = []
    for instrument in INSTRUMENTS:
        params = {
            "instrument_name": instrument,
            "start_timestamp": int(start)*1000,
            "end_timestamp": int(end)*1000,
            "resolution": 60
        }
        response = requests.get(url, params=params)
        result = response.json()["result"]
        df = pd.DataFrame({
            "timestamp": [datetime.fromtimestamp(t / 1000) for t in result["ticks"]],
            instrument: result["close"],
        })
        dataframes.append(df[df['timestamp'].dt.hour==8])

    merged_data = None
    for i, df in enumerate(dataframes):
        if merged_data is None:
            merged_data = df.copy()  # Initialize with the first df
        else:
            merged_data = pd.merge(merged_data, df, on='timestamp', how='outer')

    merged_data = merged_data.set_index('timestamp')
    return merged_data