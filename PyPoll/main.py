#create script that analyzes election_data.csv

#import os module
import os

#import csv module
import csv

#import file
csvpath = os.path.join('Resources','election_data.csv')

#set output file
pypoll_results = os.path.join('pypoll_results.txt')

with open(csvpath) as csvfile:
    datareader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)

#assign empty lists
    voterID = []
    county = []
    candidates = []

    for data in datareader:
#add items to lists 
        voterID.append(data[0])
        county.append(data[1])
        candidates.append(data[2])
#calculate total number of votes cast and print
    total_votes = len(voterID)
    print("The total number of votes cast is: " + str(total_votes))
#create complete list of all candidates who received votes
    def get_unique_candidates(candidates):
        unique_candidates = []

        for candidate in candidates:
            if candidate in unique_candidates:
                continue
            else:
                unique_candidates.append(candidate)
        return unique_candidates
    print(get_unique_candidates(candidates))
#calculate percent of votes each candidate won
#calculate total votes by candidate
#determine winner of election based on popular vote
#print results to terminal
#export results as a text file
