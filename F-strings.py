#Printing using f-strings
# Original code w/o f-strings

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

#Prints above cod ew/o converting percentage calculated into string. Instead is calculated in-line and then f-string allows it to be printed

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#----------------------------------------

# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#prints counties converting int2str

#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")

#Prints counties using f-strings

#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")


#----------------------------------------

#Multiline f-strings

#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))

#Mutliline f-string example with no formatting for percentage results

#message_to_candidate = (
#    f"You received {candidate_votes} number of votes. "
#    f"The total number of votes in the election was {total_votes}. "
#    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

#Multiline f-string example adding thousands separator and keeping voting percentage to 2 decimal points using structure: f'{value:{width},.{precision}}'
#message_to_candidate = (
#    f"You received {candidate_votes:,} number of votes. "
#    f"The total number of votes in the election was {total_votes:,}. "
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)

#----------------------------------------

#3.2.11 Skill Drill Print county and registered voter from dictionary counties_dict
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")


#3.2.11 Skill Drill print county and registered voters from list of dictionaries
#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
    #if trigger the f-string with a double quote put string markers for keys and values in single quotes
    #Found help here: https://stackoverflow.com/questions/43488137/how-to-do-a-dictionary-format-with-f-string-in-python-3-6
#     print(f"{county_dict['county']} county has {county_dict['registered_voters']} registered voters")