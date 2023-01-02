#RFC 3339
#2022-09-16T07:00:00.00+01:00
#2022-09-16T07:00:00.00+01:00
from datetime import datetime
import pandas as pd

months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", 
"Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

unpureTime = ["Sep 16, 2022",  "07:00"]

#Year
year = unpureTime[0][8:]
#Month
month = unpureTime[0][0:3]
#Dom
dom = unpureTime[0][4:6]

pureTimeArray = []

pureTime = year + "-" + months[month] + "-" + dom + "T" + unpureTime[1] + ":00.00+01:00"

df = pd.read_pickle("pure_data.pkl")

indexDF = df.to_dict(orient='index')

for eachIndex in indexDF:
    pureTime = eachIndex[8:] + "-" + months[eachIndex[0:3]] + "-" + eachIndex[4:6] + "T" + indexDF[eachIndex]["time"] + ":00.00+01:00"
    pureTimeArray.append(pureTime)

df["RFC3339"] = pureTimeArray

df.to_pickle("pure_data.pkl")