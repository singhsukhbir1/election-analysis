# The data we need to retrieve.
#1. The total number of votes cast.
#2. A Completer list of candidates who received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each cnadidate won.
#5. The winner of the election based on popular vote.


import csv
#Assign a variable for the file to load and the path.
file_to_load = "resources\election_results.csv"

#Assign a variable for the file to save and the path.
file_to_save = "analysis\election_analysis.txt"

#open the election results and read the file
with open(file_to_load) as election_data:
     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #print the header row.
    headers = next(file_reader)
    print(headers)

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, 'w') as election_analysis:
    election_analysis.write("Countries in the Election\n--------------------------------\n")
    election_analysis.write("Arapahoe\nDenver\nJefferson")