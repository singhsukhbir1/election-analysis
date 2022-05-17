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

#Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:
     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #read the header row.
    headers = next(file_reader)
       
    for row in file_reader:
        #add to the total value count
        total_votes += 1
        #get value for candidate name row
        candidate_name = row[2]
        #add candidate name to candidate option list
        if candidate_name not in candidate_options:
            #if candidate name no in list then add name
            candidate_options.append(candidate_name)
            
            #create each candidate as a key
            #begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0
        #add a vote to candidates count   
        candidate_votes[candidate_name] += 1

#save the results to our text file.
with open(file_to_save, 'w') as election_analysis:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"---------------------------------\n"
        f"Total Votes: {total_votes:,}\n"

        f"---------------------------------\n"
    )
    print(election_results, end="")
     # After printing the final vote count to the terminal save the final vote count to the text file.
    election_analysis.write(election_results)
    
    
    for candidate,votes in candidate_votes.items():
        #vote count and percentage for each candidate
        vote_percentage = float(votes)/float(total_votes) * 100
        #print the candidate name and percentage of votes
        candidate_results = (f"{candidate}: {vote_percentage:3.2f}% ({votes:,})\n")
        print(candidate_results)
        election_analysis.write(candidate_results)

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
    winning_candidate_summary = (
        f"---------------------------------\n"
        f"Winning candidate:  {winning_candidate}\n"
        f"Winning Percentage: {winning_percentage:3.2f}%\n"
        f"Winning Count:      {winning_count:,}\n"
        f"---------------------------------\n")
    # Save the winning candidate's results to the text file.
    election_analysis.write(winning_candidate_summary)


