import os
import csv

#Had one on one tutorting session with Ikaneng Malapile on 07/14/2024.
#Xpert Learning Assistant utilized for the following output below.
#AskBCSLearningAssistant utilized via Slack for troubleshooting file path directory.
# Files to load and output
file_to_load = os.path.join(r"PyPoll\Resources\election_data.csv")
file_to_output = os.path.join(r"PyPoll\analysis\election_results.txt")

# Initialize variables
total_votes = 0
candidates = []
votes_per_candidate = {}

# Read the CSV file
with open(file_to_load, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    next(csvreader)  # Skip the header row
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            votes_per_candidate[candidate] = 1
        else:
            votes_per_candidate[candidate] += 1

# Calculate the percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in votes_per_candidate.items()}

# Determine the winner based on total votes
winner = max(votes_per_candidate, key=votes_per_candidate.get)

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({votes_per_candidate[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the analysis results to a text file
with open(file_to_output, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate in candidates:
        file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes_per_candidate[candidate]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")