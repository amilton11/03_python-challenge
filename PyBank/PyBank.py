# Task is to create a Python script that analyzes the records to calculate each of the following that prints to the terminal and exports a txt file
##The total number of months included in the dataset
##The net total amount of "Profit/Losses" over the entire period
##The average of the changes in "Profit/Losses" over the entire period
##The greatest increase in profits (date and amount) over the entire period
##The greatest decrease in losses (date and amount) over the entire period

# os = operating system module
import os

# telling python the file type I am using 
import csv

# assign the file I want to reference
#mainPyBank = the scripts I am writing
mainPyBank = os.path.join("Resources", "PyBank_Resources_data.csv")

# assign the variables
profit = []
monthly_changes = []
date = []

total_months = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# opening the file 
with open(mainPyBank, newline="") as csv_file:
    
    # establish the reader
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # skip header
    csv_header = next(csv_reader)

    # Calculate total number of months included in the data set
    # Iterate through the rows in the stored file contents
    for row in csv_reader: 
            
        # count the total number of months included in the dataset
        total_months = total_months + 1
    
        # date needed for greatest increase and decrease
        date.append(row[0])

        # append profit information
        profit.append(row[0])
        total_profit = total_profit + int(row[1])

        #Calculate the average change in profits from month to month. Then calulate the average change in profits
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit

        #Store these monthly changes in a list
        monthly_changes.append(monthly_change_profits)
        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit
        
        # calculate the average change in profits
        average_change_profits = (total_change_profits/total_months)
        
        # find the max and min profit change
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)
       
        # find the dates the max and min profit change occured
        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]


 # print results      
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: " + str(total_months))
print(f"Total Profits: " + "$" + str(total_profit))
print(f"Average Change: " + "$" + str(int(average_change_profits)))
print(f"Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
print(f"Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")")

# output txt file
finanacial_analysis = os.path.join("finanacial_analysis.txt")
with open(finanacial_analysis, "w") as outfile:  

    outfile.write("Financial Analysis\n")
    outfile.write("--------------------------------\n")
    outfile.write(f"Total Months: " + str(total_months)+ "\n")
    outfile.write(f"Total Profits: " + "$" + str(total_profit))
    outfile.write(f"Average Change: " + "$" + str(int(average_change_profits))+ "\n")
    outfile.write(f"Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")" + "\n")
    outfile.write(f"Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")" + "\n") 