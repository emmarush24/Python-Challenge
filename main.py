#PyBank Challenge

#Import CSV
import os 
import csv

Total_month = 0
NetTotal = 0
NetChanges = []
GreatestIncrease = ["", 0]
GreatestDecrease = ["", 99999999999]
MonthChange = []

csvpath = os.path.join("Resources", "budget_data.csv")
print(csvpath)

#The total number of months included in the dataset
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    firstRow = next(csvreader)
    Total_month += 1 
    NetTotal += int(firstRow[1])
    PreviousNet = int(firstRow[1])
    for x in csvreader:
        #Tracking total
        Total_month += 1 
        NetTotal += int(x[1])
        #Tracking Changes
        NetChange = int(x[1]) - PreviousNet
        PreviousNet = int(x[1])
        NetChanges += [NetChange]
        MonthChange += [x[0]]
        #Tracking increase and decrease
        if NetChange > GreatestIncrease[1]:
            GreatestIncrease[0] = x[0]
            GreatestIncrease[1] = NetChange
        if NetChange < GreatestDecrease[1]:
            GreatestDecrease[0] = x[0]
            GreatestDecrease[1] = NetChange
#Calculating the average net change
AvgNetChange = sum(NetChanges)/len(NetChanges)
Answers = (f"Total Months: {Total_month}\n" 
          f"Total: {NetTotal}\n"
          f"Average Change: {AvgNetChange}\n"
          f"Greatest Increase in Profits: {GreatestIncrease}\n"
          f"Greatest Decrease in Profits: {GreatestDecrease}\n")
print(Answers)

#PyPoll Challenge
import os 
import csv

#initialize variables
TotalVotes = 0
Candidates = []
VotesPerCandidate = []
Winner = []
CandidatePercentages = []

#import the data
pypoll = os.path.join("Resources", "election_data.csv")
print(pypoll)

#read the data file
with open(pypoll) as pyfile:
    pollreader = csv.reader(pyfile, delimiter=',')
    PollHeader = next(pollreader)
    #print(PollHeader)
    #Initialize variables
    PollFirstRow = next(pollreader)
    CandidateVotes = {}
    for i in pollreader:
        #Tracking Total Votes
        TotalVotes += 1
        #Tracking Candidates:
        candidate_name = i[2]
        if candidate_name not in CandidateVotes:
            CandidateVotes[candidate_name] = 1
        else:
            CandidateVotes[candidate_name] += 1
    print(CandidateVotes)
#Calculate the percentage of votes in a new array that includes candidate name and vote count
CandidatePercentages = {candidate: (votes / TotalVotes) * 100 for candidate, votes in CandidateVotes.items()}
print(CandidatePercentages)
#Create a variable for the winner
winner = max(CandidateVotes, key=CandidateVotes.get)
#print(winner)
#print final results
print("Election Results")
print(f"----------------------")
print(f"Total Votes: {TotalVotes}")
print(f"-----------------------")
print(f"{CandidatePercentages}")
print(f"----------------------")
print(f"Winner: {winner}")

