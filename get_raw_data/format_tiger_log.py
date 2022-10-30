# -*- coding: utf-8 -*-
import os
import sys
import json
import pytz
import datetime

def in_filter(f, filter):
    for kw in filter:
        if kw in f:
            return True
    return False

def get_dir_result(dir_name, code, output_dir):
    file_list = os.listdir(dir_name)
    for f in file_list:
        print(f)
        output_items = []
        with open(dir_name+f) as f1:
            for line in f1.readlines():
                try:
                    this_items = json.loads(line)['items']
                except:
                    print(line)
                if len(this_items) > len(output_items):
                    output_items = this_items
        print(len(output_items))        
    
        ts = int(output_items[0]['time']/1000)
        tz = pytz.timezone('America/New_York')
        dt = pytz.datetime.datetime.fromtimestamp(ts, tz)
        dt = dt.strftime('%Y-%m-%d')

        with open(output_dir+dt+'_'+code, 'w+') as f_out:
            for item in output_items:
                f_out.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(int(item['time']/1000), 'null', 'null', 'null', item['price'], item['volume']))


if __name__ == "__main__":
    code = sys.argv[1]
    dir_name = "/root/program_trading/tiger_log/{}/".format(code)
    filter = []
    #filter = ["IXIC"]
    output_dir = "/root/program_trading/tiger_log_after/{}/".format(code)
    
    get_dir_result(dir_name, code, output_dir)
