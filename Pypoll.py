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
#county option and county votes
county_option= []
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#winning county and county votes and percentage trancker
winning_county = ""
winning_county_votes = 0
county_percentage = 0

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
        county_name = row[1]

        #add candidate name to candidate option list
        if candidate_name not in candidate_options:
            #if candidate name no in list then add name
            candidate_options.append(candidate_name)
            
            #create each candidate as a key
            #begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0
        #add a vote to candidates count   
        candidate_votes[candidate_name] += 1
        if county_name not in county_option:
            #if county name not in list then append  county name
            county_option.append(county_name)
            county_votes[county_name] = 0
        #track county vote count
        county_votes[county_name] += 1

#open the election analysis file in write mode
with open(file_to_save, 'w') as election_analysis:
     # After opening the file print the final vote count to the terminal.
    election_results = (
    f"\nElection Results\n"
    f"---------------------------------\n"
    f"Total Votes: {total_votes:,}\n"

    f"---------------------------------\n"
    )
    #printing vote count in terminal
    print(election_results, end="")
    #create and print County Votes Subheading
    print_county_votes = ("\nCounty Votes:  \n")
    print(print_county_votes)
     # After printing the final vote count to the terminal save the final vote count to the text file.
    election_analysis.write(election_results)
    # write County Votes Subheading
    election_analysis.write(print_county_votes)
    
    for county,c_votes in county_votes.items():
        #winning_county = ""
        #winning_county_votes = 0
        #county_percentage = 0

        #check which county is leading in vote count
        if c_votes > winning_county_votes:
            #if county votes is greater than the previous vote count
            #then
            winning_county = county
            winning_county_votes = c_votes
            #calculate percentage
            county_percentage = c_votes / total_votes * 100

        #if the above condition is no true then
        else:
            #calculate percentage if county not leading in votes
            county_percentage = c_votes / total_votes * 100

        #assign the printing format to a variable    
        winning_print = (f"{county}: {county_percentage:3.1f}% ({c_votes:,})\n")
        #printing in terminal
        print(winning_print)
        #write data in file
        election_analysis.write(winning_print)
        
    #Winning county summary format for display
    winning_county_summary = (
        f"---------------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"---------------------------------\n\n"
        )
    #print largest county turnout in termnal
    print(winning_county_summary)
    #write largest county turnout in text file
    election_analysis.write(winning_county_summary)    



       
    
    for candidate,votes in candidate_votes.items():
        #vote count and percentage for each candidate
        vote_percentage = float(votes)/float(total_votes) * 100
        #print the candidate name and percentage of votes
        candidate_results = (f"{candidate}: {vote_percentage:3.1f}% ({votes:,})\n")
        print(candidate_results)
        election_analysis.write(candidate_results)

        #determine the winning candidate
        #1. determine if votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2. if true 
            #vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #3. assign winning candidate
            winning_candidate = candidate
        else:
            pass

    #print the winner candidate, votes and percentage
    winning_candidate_summary = (
        f"---------------------------------\n"
        f"Winning Candidate:  {winning_candidate}\n"
        f"Winning Count:      {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:3.1f}%\n"
        f"---------------------------------\n")
    #print the winning candidate results in terminal
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    election_analysis.write(winning_candidate_summary)
    


