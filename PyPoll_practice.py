# End Goals
# 1. Total number of votes cast
# 2. Complete list of candidates that received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidtate won
# 5. Declare winner by number of votes

# Import modules to use
import csv
import os


# Assign a variable for the file to load and the path.

# *****Old way
# file_to_load = '/Users/joshuaallen/Documents/Boot_Camp/UCB_Projects/election-analysis/Resources/election_results.csv'

# **** New way
file_to_load = os.path.join("UCB_Projects/election-analysis/Resources", "election_results.csv")


# Open the election results and read the file using "with" statement
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

# Close the file.
election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("UCB_Projects/election-analysis/analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")


# Old way
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("UCB_Projects/election-analysis/analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file. "\n" means write to new line
     txt_file.write("Counties in the election\n-------------------------------\nArapahoe\nDenver\nJefferson")


#---------------------------------------
# PyPoll module work importing and reading file
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    for row in file_reader:
        print(row)
    
    # Retrieve first item from each row of CSV list
    # for row in file_reader:

    # print(row[0])