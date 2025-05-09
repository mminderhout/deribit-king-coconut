## Usage
```shell
python main.py 
```
- python version is 3.12
## Output
Textual output indicating on what day and at what usd price the sale of the king coconut mostl likely occurred. Additionally, the sum of squared deviations from the mean usd price is given as a measure of price equality across the crypto payment options, and the number of currencies for which there is no data at that timestamp is also given. The usd price is rounded to 2 decimals, and if it is not equal across all cryptos, the median is reported as the sale price. 

## Assumptions
- I assume the sale does not occur at a time where 2 or more of the currencies available for payment were not trading on Deribit. Initially I assumed all currencies should be trading on Deribit, but this did not lead to satisfactory results, which is why I relaxed that assumption. I'm not sure how to justify allowing 1 missing product but not 2 or more, so this is to some extent a case of hardcoding information into the script that I should not have yet. 
- I assume that /public/get_tradingview_chart_data is a good enough substitute for /private/get_settlement_history_by_instrument. The latter method likely provides exactly the data I need, but I wanted to avoid private methods so that the script can be run without any preparation or arguments (in the form of requiring Deribit accounts and API authorization). I further assume that data supplied by the former method at a resolution of 1D is sufficient, and that it is not necessary to check at a higher resolution since settlements are also daily. 

## Key Challenges
- Finding a logical timeframe for the initial search. As mentioned, I started from the time that all currencies first had a perpetual product listed on Deribit. I needed to widen this range, but could not find a new range that seemed equally logical to this one.
- Determining the resolution of historical price data. I started by importing hourly data, and selecting all observations corresponding to 08:00 UTC, since this is when (I believe) settlement occurs. This gave me problems with importing enough data in one go. I have not managed to pinpoint what the issue was, but under time constraints I decided that using a 1D resolution was sufficient.
- Determining the price. Perhaps a results of my previous point, or of using /public/get_tradingview_chart_data instead of /private/get_settlement_history_by_instrument, or simply a feature of the data, but the quoted usd price was not exactly the same for each currency even for the 'best' date. The most common quoted price was $4.21, but also $4.20 and $4.22 occurred. I decided to give the median in my answer, since the mean could introduce an extra decimal, while the assignment requires/allows rounding to 2 decimals. Initially I hoped that I could find a moment where all quoted prices were equal to 2 decimals. This could then act as a stopping condition, or prompt a more granular search if not achieved. I discontinued this approach because it seemed unlikely that I would find such an instance. 


Sadly the QR codes didn't provide any useful information to narrow down the search, though it is a nice detail that they link to Beeple's and Jeremy Sturdivant's wallets. 
