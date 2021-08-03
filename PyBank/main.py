import csv
import sys
import os
import statistics

def extractNumber(line): # extract dollar value for current month
  number=int(line[1])
  return number

def extractDate(line): #extract month/year date
  dateExtr=line[0]
  return dateExtr




ScriptFolderPath=sys.path[0].replace(os.sep, '/') #calculate folder where the script 'main' resides


with open(ScriptFolderPath +'/Resources/budget_data.csv', 'r') as f:
    
    csv_reader = csv.reader(f)
    csv_header = next(csv_reader) # skip the header and store it just in case
    
    ProfitLoss=[] # create list of profit/loss values
    Dates=[] #List to store dates
   
    for line in csv_reader:
        ProfitLoss.append(extractNumber(line))
        Dates.append(extractDate(line))

    TotalMonths=len(ProfitLoss) #The total number of months included in the dataset

    Total=sum(ProfitLoss)  #The net total amount of "Profit/Losses" over the entire period  
    
    differences= [ProfitLoss[n]-ProfitLoss[n-1] for n in range(1,TotalMonths)] #Calculate the changes in "Profit/Losses" over the entire period

    MeanDiff=round(statistics.mean(differences),2) #find the average of those changes
    MaxProfit=max(differences) #The greatest increase in profits (date and amount) over the entire period
    MaxProfitDate=Dates[differences.index(MaxProfit)+1]
    MaxLoss=min(differences) #The greatest decrease in profits (date and amount) over the entire period
    MaxtLossDate=Dates[differences.index(MaxLoss)+1]

def printAnalysis(f): # format printout of the analysis
  print("Financial Analysis",file=f)
  print("------------------",file=f)
  print(f"Total Months: {TotalMonths}",file=f)
  print(f"Total ${Total}",file=f)
  print(f"Average Change: ${MeanDiff}",file=f)
  print(f"Greatest Increase in Profits: {MaxProfitDate} (${MaxProfit})",file=f)
  print(f"Greatest Decrease in Profits: {MaxtLossDate} (${MaxLoss})",file=f)

printAnalysis(sys.stdout) # print analysis to terminal

with open(ScriptFolderPath +'/analysis/Financial_Analysis.txt', 'w') as f:
  printAnalysis(f) #print analysis to file





