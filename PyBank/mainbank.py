import os
import csv


#set varibles
total_months = []
total_profit = []
monthly_profit_change = []

#set path
csvpath = os.path.join('C:\\Users\\lorif\\Demo\\python-challenge\\PyBank\\Resources\\budget_data.csv')
#open csv file
with open(csvpath) as csvfile:

    #create csvreader variable to store budget.csv file
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header label
    header = next(csvreader)

    #loop thru the rows in the csvreader stored contents
    for row in csvreader:

        #split date to get month
        total_months.append(row[0])
        total_profit.append(int(row[1]))
        
    #loop thru profits to get monthly change
    for i in range(len(total_profit)-1):

        #difference between two months
        monthly_profit_change.append(total_profit[i+1] - total_profit[i])

#calculate max and min monthly profit list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

#correlate max and min values to correct list and index. Use 1 to change to next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

#final statements
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change), 2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

#open function to open the file "Final_Lori.txt"
#(same directory)in append mode 
#file1 = open("Final_Lori","a")
#file1.close()

#store its reference in the variable file1
# and "Final_Lori.txt" in C:
file2 = open(r"C:\\Users\\lorif\\Demo\\python-challenge\\PyBank\\analysis\\Final_Lori.txt","w+")

#write to txt file
file2.write("Financial Analysis\n")
file2.write("------------------------------\n")
file2.write(f"Total Months: {len(total_months)}\n")
file2.write(f"Total: ${sum(total_profit)}\n")
file2.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change), 2)}\n")
file2.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})\n")
file2.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})\n")

