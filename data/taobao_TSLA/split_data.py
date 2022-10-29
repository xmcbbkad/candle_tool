import pandas as pd
import csv

dt = pd.read_csv('./TSLA.csv')

last_date = ""
f = None
for i in range(len(dt)):
    
    date = dt.loc[i]['date'].split()[0]
    
    if date != last_date:
        if f:
            f.close()
        f = open("{}.csv".format(date),"w+")
        writer = csv.writer(f)
        writer.writerow(dt.columns)
        writer.writerow(dt.loc[i])
        last_date = date
    else:
        writer.writerow(dt.loc[i])
    
    if i == len(dt) -1:
        f.close()
