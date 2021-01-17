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
#assign empty lists
    profits = []
    months_number = []
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
    print(average(profits))
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