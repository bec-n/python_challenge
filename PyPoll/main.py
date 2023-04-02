# Modules
import os
import csv

# Set path for file (assuming path file is in PyPoll folder)
csvpath = os.path.join("Resources", "election_data.csv")

# Define variables 
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Open the CSV file and specify delimiter 
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read header row 
    csv_header = next(csvreader)

    # Loop through all rows 
    for row in csvreader:

        # Calculate total number of months 
        total_votes += 1

        


        
# Print the results in terminal 
print("Election Results")
print("-------------------------")
print(f"Total Months: {total_votes}")
print("-------------------------")
