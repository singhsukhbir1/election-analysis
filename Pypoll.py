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

#1. Initialize a total vote counter
total_votes = 0

#Candidate options
candidate_options = []
#declate the empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:
     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #print the header row.
    headers = next(file_reader)
    #initialize candidate votes 
    votes = 0
    
    for row in file_reader:
        #add to the total value count
        total_votes += 1
        #get value for candidate name row
        candidate_name = row[2]
        #add candidate name to candidate option list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            #create each candidate as a key
            #begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0
        #add a vote to candidates count   
        candidate_votes[candidate_name] += 1
    
    
    for candidate,votes in candidate_votes.items():
        #vote percentage for each candidate
        vote_percentage = float(votes)/float(total_votes) * 100
        #print the candidate name and percentage of votes
        print(f"{candidate}: {vote_percentage:3.2f}% ({votes:,})")

        #determine the winning candidate
        #1. determine if votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2. if true 
            #vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #3. 
            winning_candidate = candidate
        else:
            pass

    #print the winner candidate, votes and percentage
    print("---------------------------------")
    print(f"Winning candidate:  {winning_candidate}")
    print(f"Winning Percentage: {winning_percentage:3.2f}%")
    print(f"Winning Count:      {winning_count:,}")
    print("---------------------------------")




# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, 'w') as election_analysis:
    election_analysis.write("Countries in the Election\n--------------------------------\n")
    election_analysis.write("Arapahoe\nDenver\nJefferson")