
import csv
import sys
import os



ScriptFolderPath=sys.path[0].replace(os.sep, '/') #calculate folder where the script 'main' resides


with open(ScriptFolderPath +'/Resources/election_data.csv', 'r') as f:
    
    csv_reader = csv.reader(f)
    csv_header = next(csv_reader) # skip the header and store it just in case
    TotalVotes=0
    CandidatesVotes={} # initialize dictionary to store candidates and their ids of their voters
    for line in csv_reader:
        TotalVotes+=1
        CandidatesVotes.setdefault(line[2],[]).append(line[0]) # store voters ids for each candidate in a dictionary
    CandidateList=list(CandidatesVotes.keys())

    CandidateResults=[] #list to store candidate results

    votesControl=0 # check if number of votes adds up for each candidate and equal total number of votes
    for candidate in CandidateList: # calculate candidate results
        
        nVotes=len(CandidatesVotes[candidate])
        votesControl+=nVotes
        percentVotes=nVotes/TotalVotes*100
        CandidateResults.append([candidate,nVotes,percentVotes])
    if votesControl!=TotalVotes: print("Error! votes don't add up!")

    winnerVotes=max(list(zip(*CandidateResults))[1])
    winnerIdx=list(zip(*CandidateResults))[1].index(winnerVotes)
    winner=CandidateResults[winnerIdx][0]

    def printResults(f):
        print("Election Results",file=f)
        print("-------------------------",file=f)
        print(f"Total Votes: {TotalVotes}",file=f)
        print("-------------------------",file=f)
        for candidate in CandidateResults:
            print(f"{candidate[0]}: {candidate[2]:.3f}% ({candidate[1]})",file=f)
        print("-------------------------",file=f)
        print(f"Winner: {winner}",file=f)
        print("-------------------------",file=f)

    printResults(sys.stdout) # print analysis to terminal
    with open(ScriptFolderPath +'/analysis/Election_Results.txt', 'w') as f:
        printResults(f) #print analysis to file
  

    



