import os
import csv
'set the path'
csvpath = os.path.join("Resources", "budget_data.csv")

Total_months = 0
Net_Total_amount = 0



# = open("budget_data.csv","r")

'get the list of all lines in the text file'
lines = Bank_Data.readlines()

#read the whole file line by line
for i in range(0), len(lines))"
    print lines [i]"

import csv
myfile = open("C:\\Users\\your_username\\Desktop\\example1.csv", "r")  # "r" means that we only want to read the file and get the information from the file, there are couple options
csvfile = csv.reader(myfile)  # get rows in the file
for row in csvfile:  # print all rows in the file
     print row



#open csv path
with open(csvpath) as csvfile:
    #csv reader specifies delimiter and variable the holds contents
    csvreader = csv.reader(csvfile, delimiter= ',')
    
    #read the header row first
    csv_header = next(csvreader)
    




    #read each row of data after the header
    for row in csvreader:
        total_months = total_months + 1
        total_pl += int(row[1])
      # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
        changes_in_pl.append(float(row[1])
        #date.append(row[0])
        
        
        #in this loop I did total of difference between all row of column "Profit/Losses" and found total PL change. Also found out max PL change and min PL change. 
    for i in range(len(changes_in_pl)):
        #total_changes += changes_in_pl[i]
        total_changes.append(changes_in_pl[i] - changes_in_pl[i-1])   
    avg_changes = total_changes / len(changes_in_pl)
        
        
        
        print(row)

'open file'
