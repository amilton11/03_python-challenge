#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv

mainPyPoll = os.path.join(".","Resources", "PyBank_Resources_data.csv")

total_votes = 0
candidates = 0
percent_votes_won = 0
total_votes_won = 0
winner = 0

with open(mainPyPoll, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)

    row_count = sum(1 for row in csv_file)

