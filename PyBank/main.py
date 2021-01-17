#create script that analyzes budget_data.csv

#import os module
import os

#import csv module
import csv

#import file
csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    datareader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)
    #calculate average profit
    profits = []
    for data in datareader:
        profits.append(int(data[1]))
        def average(profits):
            length = len(profits)
            total = 0.0
            for profit in profits:
                total += profit
            return total / length
    print(average(profits))
    
with open(csvpath) as csvfile:
    datareader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)
    #calculate total number of months in dataset
    months_number = []
    for data in datareader:
        months_number.append(data[0])
        count = len(months_number)
    print(count)
        
with open(csvpath) as csvfile:
    datareader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)
    #calculate net total profit/loss over entire timeframe
    for data in datareader:
        sum(profits)
    print(sum(profits))


#calculate largest period increase, month and amount
#calculate largest period decrease, month and amount
#print results to terminal
#export results as a text file