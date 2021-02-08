#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

# import dependancies
import os
import csv

# create variables to capture information

# a counter
total_votes = 0

# a list
candidates = []

# a dictionary
percentage_vote_by_candidate = {}

# a dictionary
votes_per_candidate = {}

# open and read the file
with open('Resources/PyPoll_Resources_data.csv', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip the header
    next(csvreader, None)

    # create a for loop
    for row in csvreader:
        
        # count the number of total votes and increase by 1
        total_votes += 1

        # loop through csv file and gather candidates for the candidates list
        if row[2] in candidates and row[2] not in 'Candidates':
            votes_per_candidate[row[2]] = votes_per_candidate[row[2]] + 1

        else:
            candidates.append(row[2])
            votes_per_candidate[row[2]] = 1
        
# % calculation
for key, value in votes_per_candidate.items():
    percentage_vote_by_candidate[key] = str(round((value/total_votes)*100, 3)) + "% ("+str(value)+ ")"

# find the winner
winner = max(votes_per_candidate.keys(), key=(lambda k: votes_per_candidate[k]))
winner

 # print results      
print("Election Results")
print("--------------------------------")
print(f"Total votes: {total_votes}")
print("---------------------------------")
print(f"Percentage: {percentage_vote_by_candidate}")
print("------------------------------")
print(f"Winner: {winner}")
print("------------------------------")

# output txt file
election_results = os.path.join("election_results.txt")
with open(election_results, "w") as outfile:  

    outfile.write("Election Results\n")
    outfile.write("--------------------------------\n")
    outfile.write(f"Total votes: {total_votes}\n")
    outfile.write("---------------------------------\n")
    outfile.write(f"Percentage: {percentage_vote_by_candidate}\n")
    outfile.write("------------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("------------------------------\n")
