import datetime
import pytz

time_string = "2022-02-25 15:59:00 GMT-0500"
dt = datetime.datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S GMT%z')

ts = int(dt.timestamp())
print(ts)

t = datetime.datetime.fromtimestamp(ts, pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S GMT%z')
print(t)


