import os
import csv


#set varibles
candidate_list = []
total_votes = 0
total_of_candidatevotes = []
percent_of_candidatevotes = []
candidate_one_votes = 0
candidate_two_votes = 0
candidate_three_votes = 0
candidate_four_votes = 0

#set path
csvpath = os.path.join('C:\\Users\\lorif\\Demo\\python-challenge\\PyPoll\\Resources\\election_data.csv')
#open csv file
with open(csvpath) as csvfile:

    #create csvreader variable to store budget.csv file
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header label
    header = next(csvreader)

    #loop thru the rows in the csvreader stored contents
    for row in csvreader:
     
# count the total number of votes in list
        total_votes = total_votes + 1

        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            index = candidate_list.index(row[2])
            #add first vote to candidate index
            total_of_candidatevotes.append(1)

        else:
            index = candidate_list.index(row[2])
            total_of_candidatevotes[index] += 1



# complete list of candidates who recieved votes
# 
# percentage of votes for each candidate
# 
# total count of votes for each candidate
    for row in csvreader:
        if str(row[2]) == candidate_one:
            candidate_one_votes = int(candidate_one_votes) + 1
# the winner with the most votes        
        
       

#final statements
print(f"Election Results")
print("------------------------------")
print(f"Total Votes: {total_votes}")
print(f"-----------------------------")
print(f"Khan: {candidate_one_votes}")
print(f"Correy: {candidate_two_votes}")
print(f"Li: {candidate_three_votes}")
print(f"O'Tooley:{candidate_four_votes}")
print(f"-----------------------------")
#print(f"Winner: str(max(pypoll)))
print()



#store its reference in the variable file1
# and "Final_PyPoll.txt" in C:
file2 = open(r"C:\\Users\\lorif\\Demo\\python-challenge\\PyPoll\\analysis\\Final_PyPoll.txt","w+")

#write to txt file
file2.write("Election Results\n")


