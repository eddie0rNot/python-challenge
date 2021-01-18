#create script that analyzes budget_data.csv

#import os module
import os

#import csv module
import csv

#import file
csvpath = os.path.join('Resources','budget_data.csv')

#set output file
pybank_results = os.path.join('pybank_results.txt')

with open(csvpath) as csvfile:
    datareader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)
#assign empty lists
    profits = []
    months_number = []
#begin loop for calculations
    for data in datareader:
#add items to lists
        profits.append(int(data[1]))
        months_number.append(data[0])
#calculate average profit
        def average(profits):
            length = len(profits)
            total = 0.0
            for profit in profits:
                total += profit
            return total / length
    print(int(average(profits)))
#calculate sum of profits for entire period
    sum(profits)
    print(sum(profits))
#calculate total number of months in the dataset    
    count = len(months_number)
    print(count)      
#calculate largest period increase, month and amount
#calculate largest period decrease, month and amount
#print results to terminal
#export results as a text file
with open('pybank_results.txt','w') as text_file:
    text_file.writelines(["Financial Analysis \n","------------------- \n","Total Months In Review: " + str(count),"\n","Total Sales: $" + str(sum(profits)),"\n","The average profit by period is $" + str(int(average(profits))),"\n","Greatest Increase In Profits: $" + str(max(profits)) + " TBD","\n","Greatest Decrease In Profits: $" + str(min(profits)) + " TBD","\n"])