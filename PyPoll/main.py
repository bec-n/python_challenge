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

        # Obtain first candidate name in the third column
        candidate = row[2]

        # Check if candidate in dictionary list and increment votes 
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Count votes for each candidate and % votes
for candidate in candidates:

    votes = candidates[candidate]
    percentage = (votes/total_votes)*100
    candidates[candidate] = [votes, percentage]

# Print the results in terminal 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    votes, percentage = candidates[candidate]
    print(f"{candidate}: {percentage:.2f}%")
