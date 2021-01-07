import os
import csv

mainPyPoll = os.path.join(".","Resources", "PyBank_Resources_data.csv")

total_votes = 0

with open(mainPyPoll, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)

    for row in open("csv_file"):
        total_votes += 1

        print(total_votes)