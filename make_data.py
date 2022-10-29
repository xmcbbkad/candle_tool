import pandas as pd
import csv
import time
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def make_1mins_file2dir(input_file, output_dir):
    dt = pd.read_csv(input_file)

    last_date = ""
    f = None
    for i in range(len(dt)):
        date = dt.loc[i]['date'].split()[0]
        
        if date != last_date:
            if f:
                f.close()
            logger.info(date)
            f = open("{}/{}.csv".format(output_dir, date),"w+")
            writer = csv.writer(f)
            writer.writerow(dt.columns)
            writer.writerow(dt.loc[i])
            last_date = date
        else:
            writer.writerow(dt.loc[i])
    
        if i == len(dt) -1:
            f.close()

def str2ts(string, pattern="%Y-%m-%d %H:%M:%S"):
    timeArray = time.strptime(string, pattern)
    ts = int(time.mktime(timeArray))
    return ts

def make_5mins_from_1mins_file2file(input_file, output_file):
    dt = pd.read_csv(input_file)

    f = open(output_file, 'w+')
    writer = csv.writer(f)
    writer.writerow(['date','open','high','low','close','volume'])

    last_time = ""
    open_ = 0
    high = 0
    low = 9999
    close = 0
    volume = 0
    for i in range(len(dt)):
        if last_time == "":
            last_time = dt.loc[i]['date']
            close = dt.loc[i]['close']
            high = dt.loc[i]['high']
            low = dt.loc[i]['low']

        if abs(str2ts(dt.loc[i]['date'])- str2ts(last_time)) < 4*60:
            high = dt.loc[i]['high'] if dt.loc[i]['high'] > high else high
            low = dt.loc[i]['low'] if dt.loc[i]['low'] < low else low
            volume += dt.loc[i]['volume']
        elif abs(str2ts(dt.loc[i]['date'])-str2ts(last_time)) == 4*60:
            open_ = dt.loc[i]['open']
            high = dt.loc[i]['high'] if dt.loc[i]['high'] > high else high
            low = dt.loc[i]['low'] if dt.loc[i]['low'] < low else low
            volume += dt.loc[i]['volume']
            row = [last_time, open_, high, low, close, volume]
            writer = csv.writer(f)
            writer.writerow(row)
            
            last_time = ""
            open_ = 0
            high = 0
            low = 9999
            close = 0
            volume = 0

        else:
            logger.error("wrong_data:{} {}".format(input_file, last_ts))
    f.close()

def make_5mins_from_1mins_dir2dir(input_dir, output_dir):
    for file in os.listdir(input_dir):
        input_file = os.path.join(input_dir, file)
        output_file = "{}/{}".format(output_dir, file.split('/')[-1])
        logger.info(output_file)
        make_5mins_from_1mins_file2file(input_file, output_file)


if __name__ == '__main__':
    #make_5mins_from_1mins_file2file(input_file = "/Users/xiaokunfan/programme_trading/candle_tool/data/taobao_TSLA/1min/2022-02-25.csv", output_file = "/Users/xiaokunfan/programme_trading/candle_tool/data/taobao_TSLA/5min/2022-02-25.csv")
    make_5mins_from_1mins_dir2dir(input_dir='/Users/xiaokunfan/programme_trading/candle_tool/data/taobao_TSLA/1min', output_dir = '/Users/xiaokunfan/programme_trading/candle_tool/data/taobao_TSLA/5min/')
    #make_1mins_file2dir(input_file='/Users/xiaokunfan/programme_trading/candle_tool/data/taobao_TSLA/TSLA.csv', output_dir='/Users/xiaokunfan/programme_trading/candle_tool/data/taobao_TSLA/1min')
