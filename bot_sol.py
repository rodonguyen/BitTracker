import ccxt
import config
import supertrend_bot

account = ccxt.binance({
    "apiKey": config.API_BINANCE,
    "secret": config.SECRET_BINANCE,
})

bot_matic = supertrend_bot.SupertrendBot(
                account=account,
                coinpair='SOL/AUD',
                trade_log_path='log/trade_log_bot_sol.txt',
                length = 15, multiplier = 18,
                is_in_position=True, 
                position=3.937, 
                lot=50,
                timeframe='15m',
                timeframe_in_minutes=15)

# print('\n', bot_matic.get_supertrend_data().tail(100), '\n')
bot_matic.run_forever()