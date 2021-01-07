#mainPyBank
# Task is to create a Python script that analyzes the records to calculate each of the following that prints to the terminal and exports a txt file
##The total number of months included in the dataset
##The net total amount of "Profit/Losses" over the entire period
##The average of the changes in "Profit/Losses" over the entire period
##The greatest increase in profits (date and amount) over the entire period
##The greatest decrease in losses (date and amount) over the entire period

# os is the file reference
import os

# telling python the file type I am using 
import csv

# assign the file I want to reference
#mainPyBank = the scripts I am writing
mainPyBank = os.path.join(".", "PyBank_Resources_data.csv")

# assign the variables
total_months = 0
net_profit_loss = 0
change_profit_loss = []
change_date = []
greatest_increase = []
greatest_decrease = []

# opening the file in "read" "r" mode and simplify the file name reference
with open(mainPyBank, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # skip header
    csv_header = next(csv_file)

    # Calculate total number of months included in the data set
    # Iterate through the rows in the stored file contents
    for row in csv_reader: 
            
        ##The total number of months included in the dataset
        #date.append(row 0)
        #print(date)
        total_months +=1
    

        ##The net total amount of "Profit/Losses" over the entire period
        # Calculate net total amount of "Profit/Losses" over the entire period
        # Iterate through the rows in the stored file contents
        net_profit_loss += int(row[1])
        
        ##The average of the changes in "Profit/Losses" over the entire period
        # Calculate average of the changes in "Profit/Losses" over the entire period
        # Iterate through the profits in order to get the monthly change in profits
        change_profit_loss.append(int(row[1]))
        change_date.append(row[0])
        
        ##The greatest increase in profits (date and amount) over the entire period
        # Calculate greatest increase in profits (date and amount) over the entire period
        # Obtain the max and min of the the montly profit change list
        greatest_increase = max(change_profit_loss)
        greatest_decrease = min(change_profit_loss)

        ##The greatest decrease in losses (date and amount) over the entire period
        # Calculate greatest decrease in losses (date and amount) over the entire period
        # Correlate max and min to the proper month using month list and index from max and min
        # We use the plus 1 at the end since month associated with change is the + 1 month or next month
        #max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
        #max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

ave_profit = net_profit_loss/total_months
#Financial Analysis
print(total_months)
print(net_profit_loss)
#print(change_profit_loss)
print(ave_profit)
print(greatest_increase)
print(greatest_decrease)