import mplfinance as mpf
import pandas as pd
daily = pd.read_csv('/Users/xiaokunfan/programme_trading/candle_tool/data/taobao_TSLA/2022-02-25.csv',index_col=0,parse_dates=True)
daily.index.name = 'Date'
mpf.plot(daily,type='candle',mav=(3,6,9),volume=True,show_nontrading=True)
