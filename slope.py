from scipy.stats import linregress
import pandas as pd

t = pd.read_csv('/Users/Michael/Downloads/test.csv');

columnNames = list(t.columns.values)
print(columnNames)

# get the month corresonding Y-value
date = t['Date']
y = t['HSI return']

monthY = dict()
monthDate = dict()

month = "0"

for k in range(len(date)):
    dateParsed = date[k].split("/")
    # if (dateParsed[0] != )
    if (dateParsed[0] not in monthY):
        monthY[dateParsed[0]] = list()
    monthDate[dateParsed[0]] = dateParsed[2]
    monthY[dateParsed[0]].append(y[k])

for i in range(len(columnNames)):
    if i<=1:
        continue
    print(columnNames[i])
    x = t[columnNames[i]]

    monthX = dict()
    for k in range(len(date)):
        dateParsed = date[k].split("/")
        if (dateParsed[0] not in monthX):
            monthX[dateParsed[0]] = list()
        monthX[dateParsed[0]].append(x[k])


    for key in monthDate:

        print(columnNames[i],monthDate[key]+"/"+key, linregress(monthX[key], monthY[key]).slope)
