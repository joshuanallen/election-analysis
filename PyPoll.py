# Add dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv") #******* Change to Run in Integrated terminal instead of run python might fix the reference issue
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Assign object to hold candidate names
candidate_options = []

# Create dictionary to hold candidate names and vote totals
candidate_votes = {}

# 1. Initialize total_votes variable to zero outside with open() statement to initialize to zero every time before we open the file
total_votes = 0

# Initiate variables for winning_candidate, winning_count and winning_percentage
winning_count = 0
winning_percentage = 0
winning_candidate = ""

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)

    # Iterate through each row in the CSV file.
    for row in file_reader:
    
        # 2. Add to the total vote count.
        total_votes += 1
        
        # Print the candidate name from each row
        candidate_name = row[2]

        # Ensure candidates name is not already added to candidate_options list
        if candidate_name not in candidate_options:
            
            # If name is not it candidate_options list append candidate name to candidate_options list
            candidate_options.append(candidate_name)

            # After IDing a new candidate name begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0
        
         # Add vote to respective candidate's count
        candidate_votes[candidate_name] += 1

# Print total votes (reflects total number of data points)
# print(total_votes)

# Print list of candidates
# print(candidate_options)

# Print candidate_votes dictionary which holds each candidate name and respective vote count {key = candidate's name : value = vote count}
# print(candidate_votes)

# iterate through candidate_options list to retrieve candidate's names
for candidate_name in candidate_votes:
    
    # retrieve vote count for each candidate
    votes = candidate_votes[candidate_name]

    # calculate percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # iterate through candidate_votes to find votes > 0
    if (votes > winning_count):
    # if true then votes = winning_count & vote_percentage = winning_percentage
        winning_count = votes
        winning_percentage = vote_percentage
    # select winning candidate from candidate_options list
        winning_candidate = candidate_name

    # Output candidates' names and percentage of votes (* SkillDrill:  percentage limited to 1 floating decimal)
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

# Create winning candidate output
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)