# Modules
import os
import csv

# Set path for file (assuming path file is in PyBank folder)
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV file and specify delimiter 
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row 
    csv_header = next(csvreader)

    total_months = len(list(csvreader))
    print("Financial Analysis")
    print("--------------------------------------")
    print("Total Months:", total_months)

    # Read each row of data after the header 
    
