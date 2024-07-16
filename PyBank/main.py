import os
import csv

#Had one on one tutorting session with Ikaneng Malapile on 07/14/2024.
#Xpert Learning Assistant utilized for the following output below.
#AskBCSLearningAssistant utilized via Slack for troubleshooting file path directory. 
# Files to load and output (Remember to change these)
file_to_load = os.path.join(r"PyBank\Resources\budget_data.csv")
file_to_output = os.path.join(r"PyBank\analysis\budget_analysis.txt")

# Initialize variables
total_months = 0
net_total = 0
profit_losses = []
months = []
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(file_to_load, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Skip the header row
    for row in csvreader:
        # Calculate total months and net total
        print(row)
        total_months += 1
        net_total += int(row[1])
        profit_losses.append(int(row[1]))
        months.append(row[0])

# Calculate changes in profit/losses
for i in range(1, len(profit_losses)):
    change = profit_losses[i] - profit_losses[i - 1]
    changes.append(change)

# Calculate average change
average_change = sum(changes) / len(changes)

# Identify greatest increase and decrease
for i in range(len(changes)):
    if changes[i] > greatest_increase[1]:
        greatest_increase = [months[i + 1], changes[i]]
    if changes[i] < greatest_decrease[1]:
        greatest_decrease = [months[i + 1], changes[i]]

# Print analysis results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export the analysis results to a text file
with open(file_to_output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")