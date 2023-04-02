# Modules
import os
import csv

# Set path for file (assuming path file is in PyBank folder)
csvpath = os.path.join("Resources", "budget_data.csv")

# Define variables 
total_months = 0
total_profit = 0
profit_changes = []
previous_profit = 1088983
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

# Open the CSV file and specify delimiter 
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read header row 
    csv_header = next(csvreader)

    # Loop through all rows 
    for row in csvreader:

        # Calculate total number of months 
        total_months += 1
        
        # Calculate total profit / loss in second column
        total_profit += int(row[1])
        
        # Calculate the change in profit/loss vs previous month 
        profit_change = int(row[1]) - previous_profit
        profit_changes.append(profit_change)
        
        # Check if greatest increase or decrease 
        if profit_change > greatest_increase["amount"]:
            greatest_increase["date"] = row[0]
            greatest_increase["amount"] = profit_change
        elif profit_change < greatest_decrease["amount"]:
            greatest_decrease["date"] = row[0]
            greatest_decrease["amount"] = profit_change
        
        # Reset previous_profit as the current row for the next row
        previous_profit = int(row[1])
        
# Calculate average change in profit/loss
# Total months - 1 as the first month has no change
average_profit_change = sum(profit_changes) / (total_months - 1)

# Print the results in terminal 
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${round(average_profit_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Print the results in text 