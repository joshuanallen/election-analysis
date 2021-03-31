# Election analysis using Python

## Project Overview
The Colorado Board of Elections has requested an audit of the voting data. They've provided the voter ID, county in which the vote was cast, and candidate choice for each vote. They've requested the following:
1. Calculate total votes cast
2. Names of all candidates who received votes
3. Calculate total votes for each candidate
4. Calculate the percentage of total votes each candidate received
5. Determine the winner of the election based on number of votes received

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.54.3

## Summary
Election results are in Picture 1.1 below.

**Picture 1.1:** Colorado congressional election results summary

![Colorado Congressional Election Results Summary](https://github.com/joshuanallen/election-analysis/blob/e632a5361f4356b815bb1abdaf2bd70cae478122/analysis/election_results_output.png)

### Analysis of election results by candidate
- **Total votes cast:** 369,711
- **Candidates receiving votes:**
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- **Results for each candidate:**
    - Charles Casper Stockham received **23.0%** of the vote and **85,213** in total votes.
    - Diana DeGette received **73.8%** of the vote and **272,892** in total votes.
    - Raymon Anthony Doane received **3.1%** of the vote and **11,606** in total votes.
- **Winner of the election:**
    - The winner of the election is Diana DeGette, who received **73.8%** and **272,892** votes of the total votes cast in this election.

## Challenge Overview
In addition to determining the results of the election, the Board has requested an audit of the voting data by county. They've requested the additional voting data below:
1. Calculate voter turnout for each county
2. Calculate the percentage of total votes from each individual county
3. Calculate county with highest turnout

## Challenge Summary

### Analysis of election results by county
- **Total votes by county:**
    - Jefferson County's **38,855** votes accounted for **10.5%** of the total vote count.
    - Denver County's **306,055** votes accounted for **82.8%** of the total vote count.
    - Arapahoe County's **24,801** votes accounted for **6.7%** of the total vote count.
- **County with highest turnout:**
    - Denver County had the highest voter turnout

## Use of script for future elections in Colorado
The script written to analyze the provided election data can be more widely used by the Colorado Board of Elections in any future election.

### Repurposing of current variables
This script is scalable to intake any election data and break it out by location, whether it's city, district, or regional level data. For example, in a city-wide election, the script can be altered to show results by borough. In this case, we would repurpose the objects associated with "county" data and rename them to output election data broken out by borough. To repurpose or current script, we would need to alter the following lines.

### Repurposing of script to include additional data
This script can be altered to intake additional data columns and allow for more slicing of the election data. For example, we can ingest demographic data in an additional column allowing us to break out the election results and provide a summary for each individual demographic.

We can separate the demographic data (e.g.gender) using a similar code structure analyzing the county level data seen below.

At line 23 we can intialize demographic list and dictionary.

    gender_options = []
    gender_votes = {}

Within the for loop reading the csv file line-by-line, at line 52 we would need to add the following to extract the demograpic data from an additional column.

    gender_id = row[3]

Next, we can populate the gender list and dictionaries based on the voting data by adding a if statement at line 76.

    if gender_id not in gender_options:

        gender_options.append(gender_id)

        gender_votes[gender_id] = 0

    gender_votes[gender_id] += 1

After the list and dictionary for the gender demographic data is populated, we can print our results to the terminal and text file after line 109.

    for gender_id in gender_votes:

        votesGender = gender_votes.get(gender_id)

        votesGender_percentage = float(votesGender)/float(total_votes) * 100

        gender_results = (

            f"-------------------------\n"

            f"{gender_id}: {votesGender_percentage:.1f}% ({votesGender:,})\n")

        print(gender_results)

        txt_file.write(gender_results)

The above code is easily scalable to ingest almost any string-based demographic information except age groups which would require additional script to create the age groupings.

### Limitations of current script
The script in its current form is limited in it's slicing ability. Currently, it can only slice and output based on one set of parameters. Refactoring the code to allow for multiple layers of slicing would provide us with more granular election data results. Additionally, this code is set to only yield results in direct single-winner popular vote elections. The code would have to be refactored for elections involving multiple winners or ranked-choice voting systems.
