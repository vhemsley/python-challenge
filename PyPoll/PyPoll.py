#!/usr/bin/env python
# coding: utf-8

# In[22]:


# PyPoll

# Dependencies
import csv 
import os

#Files to load and output
file_to_load = os.path.join ("election_data.csv")
file_to_output = os.path.join ("election_thorough_analysis.txt")

#Total Vote Counter 
total_votes = 1

#Candidate options and Vote Counter
candidate_options = []
candidate_votes = {}

#Winning Candidate and WInning Count Tracker
winning_candidate = ""
winning_count = 0

#Read the csv and convert it into a list
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    #Read the header
    header = next(reader)
    
    for row in reader:
        
        #Run the loader animation 
        
        #Add to total vote count
        total_votes_count = total_votes + 1
        
        #Extract the candidate name from each row 
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate... 
        # (In a way our loop  is discovering candidates as it goes )
        
        if candidate_name not in candidate_options:
            #Add it to the list of candidates in the running
            candidate_options.append(candidate_name)
            
            #begin tracking that candidate voter count
            candidate_votes[candidate_name] = 0 
            
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1 
with open(file_to_output, "w") as txt_file:
        #print the final vote count
        
        election_results = ( 
        
        f"\n\Election Results\n" +
        f"===================\n" +
        f"Total Votes: " + str(total_votes) + "\n" +
        f"===================\n"
        )
        
        # Save final vote count to text file
            
        txt_file.write(election_results)
            
        # Determine the winner by looping through the counts
            
        for candidate in candidate_votes:
        
            # Retrieve vote count and percentage
            votes = candidate_votes.get(candidate)
            vote_percentage = float(votes) / float(total_votes) * 100
            
            # Determine winning vote count and candidate
            if (votes > winning_count): 
                winning_count = votes
                winning_candidate = candidate
            
            #print each candidate's voter count and percentage to terminal 
            voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
            
            print(voter_output, end="")
            
            txt_file.write(voter_output)
            
        # Print the winning candidates
            
            winning_candidate_summary = ( 
            
            f"=======================\n"
            f"Winner: {winning_candidate}\n"
            f"=======================\n"
            
            )
            
            print(winning_candidate_summary)
        


# In[ ]:





# In[ ]:




