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
from collections import defaultdict

TotalVotes = 0
Candidates = []
VotesPerCandidate = []
Winner = []


pypoll = os.path.join("Resources", "election_data.csv")
print(pypoll)

CandidateVotes = defaultdict(int)

with open(pypoll) as pyfile:
    pollreader = csv.reader(pyfile, delimiter=',')
    PollHeader = next(pollreader)
    print(PollHeader)
    PollFirstRow = next(pollreader)
    TotalVotes +=1
    CandidateList = []
    for i in pollreader:
        #Tracking Total Votes
        TotalVotes += 1
        #Tracking Candidates:
        CandidateList.append(i[2])
        FutureCandidate = next(CandidateList)
        if CandidateList != FutureCandidate:
            Candidates.append(i[2])
    Candidate1 = Candidates[0]
    Candidate2 = Candidates[1]
    Candidate3 = Candidates[2]
    CandidateCount = []
    Candidate1Count = 0
    Candidate2Count = 0
    Candidate3Count = 0
    for j in pollreader:
        if j[2] == Candidate1:
            Candidate1Count += 1
        elif j[2] == Candidate2:
            Candidate2Count += 1
        else:
            Candidate3Count =+1
    CandidateCount.append(Candidate1Count, Candidate2Count, Candidate3Count)
Candidate1Percent = Candidate1Count/TotalVotes        
Candidate2Percent = Candidate2Count/TotalVotes
Candidate3Percent = Candidate3Count/TotalVotes     
VotesPerCandidate.append(Candidate1, Candidate1Percent, Candidate1Count, Candidate2, Candidate2Percent, Candidate2Count, Candidate3, Candidate3Percent, Candidate3Count)       

print(f"Election Results\n"
      f"------------------\n"
      f"Total Votes: {TotalVotes}\n"
      f"------------------\n"
      f"{VotesPerCandidate}\n"
      f"------------------\n")
if Candidate1Count > Candidate2Count & Candidate3Count:
    print(f"Winner: {Candidate1}")
elif Candidate2Count > Candidate1Count & Candidate3Count:
    print(f"Winner: {Candidate2}")
else:
    print(f"Winner: {Candidate3}")
