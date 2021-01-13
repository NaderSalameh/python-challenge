import os, csv 

# path to the budget csv
csv_path = os.path.join('Resources', 'budget_data.csv')

# reading the cvs file 
with open(csv_path, 'r') as csvfile:

    # splitting the data with commas 
    csv_reader = csv.reader(csvfile, delimiter=',')

    #skipping the header
    next(csv_reader)

    #Creating my lists
    months = []
    amount = []

    # creating a for loop to append to my lists 
    for row in csv_reader:
        months.append(row[0])
        amount.append(int(row[1]))

    # fancy list comprehension just because,  in order to find the change 
    change = [amount[i] - amount[i -1] for i in range(1, len(amount))]

    # capturing the greatest increase in profits 
    maxVal = max(change)
    maxValIndex = change.index(maxVal)
    maxValMonth = months[maxValIndex + 1] # doing an offset to find the index since we start from index 1 to find the changes 

    #capturing the greatest decrease in profits
    minVal = min(change) 
    minValIndex = change.index(minVal)
    minValMonth = months[minValIndex + 1] # likewise, doing another offset to find the index since we start from index 1 to find the changes 

    print("Financial Analysis")
    print("--.--------.----------.\n")
    print(f"Total Months: {len(months)}")
    print(f"Total Amount: ${sum(amount)}")
    print(f"Average Change: ${round(sum(change)/len(change),2)}")
    print(f"Greatest Increase in Profits: {maxValMonth} (${maxVal})")
    print(f"Greatest Increase in Profits: {minValMonth} (${minVal})")

# Creating an output text file 
output_path = os.path.join('Analysis', "Budget_Analysis.txt")
with open(output_path, 'w', newline='') as textfile:

    textfile.write("Financial Analysis\n")
    textfile.write("--.--------.----------.\n")
    textfile.write(f"Total Months: {len(months)}\n\n")
    textfile.write(f"Total Amount: ${sum(amount)}\n\n")
    textfile.write(f"Average Change: ${round(sum(change)/len(change),2)}\n\n")
    textfile.write(f"Greatest Increase in Profits: {maxValMonth} (${maxVal})\n\n")
    textfile.write(f"Greatest Increase in Profits: {minValMonth} (${minVal})\n\n")
