# My personal notes

## Roadmap

Week 1 (04/07)
- Write buy/sell logic: Create TP mechanism for Supertrend - Done
- Check the math after TP and trendChange - Done. TP at 1:1 cut a part of the profit while most of which is achieved in very long trend. Additionally, such long trends are not many. Thus, less profit in the end.
- Back-test Supertrend, observe results with different config as well (length, multiplier (maybe 1->5)) - Done

Week 2 (18/7):
- Use ccxt to forward-test / Create class as an account 
- Forward testing (with variable 'balance'?)

Week 3 (25/7):
- Use test API ByBit for forward testing, compare result after 2 weeks with shorten past data of the same length.

Week 4 (29/8/2022):
- Use real API Binance with little money (Current Profit/Loss: +6.5)
- Use larger historical data to find optimal configuration https://docs.coinapi.io/#limits

Week 5 (05/09/2022)
- Get top10 config, average loss, % config loss
- Plot balance vs config; pnl distribution of top10

Week 39 / 2022:
- Choose 10 configs that are in toplist config and have the highest balance: Check [`sandbox/backtest_result/best_configs_backtest_btc.csv`](sandbox/backtest_result/best_configs_backtest_btc.csv)
- Analyse BitTracker performance in bear/recent-year periods on BTC/USD with best configs found: Risk is pretty large (max -90%) in a bear market, but acceptable compared to the profit in a bull market (+200%)

Week 40 / 2022:
- Calculate [risk-adjusted return](https://www.investopedia.com/terms/r/riskadjustedreturn.asp) / [Calmar Ratio](https://www.investopedia.com/terms/c/calmarratio.asp) to choose best config
- Quickly re-evaluate coins on bear market (should only use Top10 cryptocurrency as others are not reliable in the long-term)


Stage 1: Front-end
- 📍 Display backtest on Web App using https://dygraphs.com/ + JS
- Re-plan final product (what functionalities, features is it going to have?)


Future:
- More buttons and inputs to operate bot from web app
- ALGO: Code Nadaraya-Watson estimator + Try trade logic for Nadaraya-Watson + Supertrend
- ALGO: Use deep learning (e.g., LSTM) 
- Alarm for every execution 
- Front-end trade visualisation: https://dygraphs.com/



## Notes in implemetation
- Filled position is different from calculated position (e.g. position = lot / price). It's safer to update position from executed order's returned result. Good for trade log and avoid getting error for selling more than what you actually bought.
- Exchange requires >1 second or much more to update its prices. So if you request prices miliseconds right after the candle closes, you WILL NOT get the latest price candle (latest price row). [Read more here.](https://docs.ccxt.com/en/latest/manual.html#notes-on-latency)
- Choosing the optimal configuration when trading on small timeframe (e.g. 15m) require large historical data. Because 1000 data points of 15m timeframe only covers ~10 days, which is very bias (specifically, what if it's downtrend during that period)


## Others
- Price API: https://messari.io/api/docs
- TA-Lib (Python): https://mrjbq7.github.io/ta-lib/
- Toi di code dao: https://www.youtube.com/watch?v=WlO4lkvyLvI
- Indicator: https://github.com/thanhnguyennguyen/trading-indicator 
- Visualisation: https://github.com/yongghongg/stock-screener/blob/main/supertrend_demo_medium.ipynb / https://medium.datadriveninvestor.com/the-supertrend-implementing-screening-backtesting-in-python-70e8f88f383d


## Mics bookmarks of CAB420
- https://towardsdatascience.com/how-to-get-started-building-a-stock-cryptocurrency-forex-trading-program-2abbf0a4729f
- https://thecitadelpub.com/elons-lethal-mistake-predicting-the-stock-price-of-tesla-with-twitter-and-machine-learning-5e89282ce75f
- https://medium.datadriveninvestor.com/get-up-to-date-financial-ratios-p-e-p-b-and-more-of-stocks-using-python-4b53dd82908f
- https://www.youtube.com/watch?v=xfzGZB4HhEE
- https://www.youtube.com/watch?v=z9wt01WW9go&list=WL&index=100
- https://towardsdatascience.com/machine-learning-for-day-trading-27c08274df54
- https://www.mdpi.com/2673-2688/2/4/30/htm

