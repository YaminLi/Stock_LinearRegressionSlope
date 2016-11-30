from scipy.stats import linregress
import pandas as pd

t = pd.read_csv('/Users/Michael/Downloads/Book3.csv');

columnNames = list(t.columns.values)

# get the month corresonding Y-value
date = t['Date']
y = t['HSI return']

month = "0"
year = "0"

stockSlope = dict()

for i in range(len(columnNames)):
    if i<=1:
        continue
    # print(columnNames[i])
    x = t[columnNames[i]]

    stockSlope[columnNames[i]] = list()

    yearMonth = list()
    monthX = list()
    monthY = list()
    for k in range(len(date)):
        dateParsed = date[k].split("/")
        if (k==0 or dateParsed[0] == month):
            month=dateParsed[0]
            monthX.append(x[k])
            monthY.append(y[k])
            year = dateParsed[2]
        else:
            yearMonth.append(year+"/"+month)
            stockSlope[columnNames[i]].append(linregress(monthX, monthY).slope)
            print(columnNames[i],year+"/"+month, linregress(monthX, monthY).slope)
            monthX = list()
            monthY = list()
            month = dateParsed[0]
            monthX.append(x[k])
            monthY.append(y[k])
            year = dateParsed[2]
        if (k == len(date)-1 and len(monthX)>0):
            yearMonth.append(year+"/"+month)
            stockSlope[columnNames[i]].append(linregress(monthX, monthY).slope)
            print(columnNames[i],year+"/"+month, linregress(monthX, monthY).slope)

# raw_data = dict()
raw_data = {"Date":yearMonth}
for i in range(len(columnNames)):
    if (i<=1):
        continue
    # print(len(yearMonth))
    # print(len(stockSlope[columnNames[i]]))
    raw_data[columnNames[i]] = stockSlope[columnNames[i]]

df = pd.DataFrame(raw_data)
df.to_csv('res.csv')
