# -*- coding: utf-8 -*-
import requests
import datetime
#import sys
#reload(sys)
#sys.setdefaultencoding( "utf-8" )

#file_name = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
file_name = datetime.datetime.now().strftime('%Y-%m-%d')

with open("../tiger_log/{}_{}".format(file_name, "TSLA"), 'a+') as f:
    r = requests.get("https://www.laohu8.com/proxy/stock/stock_info/time_trend/day/TSLA")
    f.write(r.text) 
    f.write('\n')

#with open("tiger_log/{}_{}".format(file_name, "BABA"), 'a+') as f:
#    r = requests.get("https://www.laohu8.com/proxy/stock/stock_info/time_trend/day/BABA")
#    f.write(r.text) 
#    f.write('\n')

#with open("tiger_log/{}_{}".format(file_name, "JD"), 'a+') as f:
#    r = requests.get("https://www.laohu8.com/proxy/stock/stock_info/time_trend/day/JD")
#    f.write(r.text) 
#    f.write('\n')
#
#with open("tiger_log/{}_{}".format(file_name, "PDD"), 'a+') as f:
#    r = requests.get("https://www.laohu8.com/proxy/stock/stock_info/time_trend/day/PDD")
#    f.write(r.text) 
#    f.write('\n')

#with open("tiger_log/{}_{}".format(file_name, "NIO"), 'a+') as f:
#    r = requests.get("https://www.laohu8.com/proxy/stock/stock_info/time_trend/day/NIO")
#    f.write(r.text) 
#    f.write('\n')
#
#with open("tiger_log/{}_{}".format(file_name, "AAPL"), 'a+') as f:
#    r = requests.get("https://www.laohu8.com/proxy/stock/stock_info/time_trend/day/AAPL")
#    f.write(r.text) 
#    f.write('\n')

#with open("tiger_log/{}_{}".format(file_name, "FB"), 'a+') as f:
#    r = requests.get("https://www.laohu8.com/proxy/stock/stock_info/time_trend/day/FB")
#    f.write(r.text)
#    f.write('\n')
 
#with open("tiger_log/{}_{}".format(file_name, "MSFT"), 'a+') as f:
#    r = requests.get("https://www.laohu8.com/proxy/stock/stock_info/time_trend/day/MSFT")
#    f.write(r.text)
#    f.write('\n')
# 
#with open("tiger_log/{}_{}".format(file_name, "AMZN"), 'a+') as f:
#    r = requests.get("https://www.laohu8.com/proxy/stock/stock_info/time_trend/day/AMZN")
#    f.write(r.text) 
#    f.write('\n')

with open("tiger_log/{}_{}".format(file_name, "IXIC"), 'a+') as f:
    r = requests.get("https://www.laohu8.com/proxy/stock/stock_info/time_trend/day/.IXIC")
    f.write(r.text) 
    f.write('\n')
