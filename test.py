#Import Statements 
import pandas as pd
from pandas_datareader import data, wb
import datetime
import os
import csv
import sys

#type in argument in terminal
filename = sys.argv[1]
list_of_top_stocks = []

#Resetting files
os.remove("stockbotOutput1.csv")
os.remove("stocks.txt")

#Opens input file and reads everyline, making sure to
#remove all "stocks" that are more than 5 letters long
with open(filename) as f:
    for each in f:
        if len(each) <= 6:
            list_of_top_stocks.append(each[:-1])

#Gives last date
start = pd.to_datetime('2021-01-16')
end = pd.to_datetime('today')
stockfile = open("stocks.txt","a")

#Datareader checks for stock info, if doesn't exist stock_info = ok
for each in list_of_top_stocks:
    stock_info = ""

    try:
        ok = str(data.DataReader(each, 'yahoo', start , end))

    except:
        ok = "N"

    stock_info = ok
    if stock_info != "N":
        stockfile.write(each + "\n")
        stockfile.write(stock_info + "\n")
    # add to csv file
stockfile.close()

#Writes to stocks.txt and converts to csv ready form
f = open("stocks.txt", "r")

ok = []
for each in f:
    conv = str(each)
    counter = 0
    if len(conv) <= 6 and len(conv) != 0:
        ok.append(str(conv[:-1]))
    for word in conv.split():
        if word.replace('.','',1).isdigit():
            ok.append(str(word))

# Writes to csv 
chunks = [ok[x:x+7] for x in range(0, len(ok), 7)]

fields = ["Company", "High", "Low", "Opening Price", "Closing Price", "Volume", "Adj Close"]

filename = "stockbotOutput1.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(chunks)
