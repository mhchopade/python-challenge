import csv
import os
from statistics import mean

csvpath = os.path.join('resources', 'budget_data.csv')
output_file = os.path.join('resources', 'Financial_Analysis.txt')

with open(csvpath, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Defining our dictionaries and lists
    dates = {}
    monthlyRev = []
    final = {}
    analysis = []

    # Builds our dictionary with profit/loss
    for row in csvreader:
        if row[0] != 'Date':
            dates[row[0]] = int(row[1])

    # Variable for total number of months, i.e., entries within the 'dates' dictionary
    totalMonth = len(dates)
    # Total net amount of profit/loss over the entire period
    totalRevenue = sum(dates.values())

    revenue = tuple(dates.values())
    month = tuple(dates.keys())

    # Adds revenue into our list
    for x in range(1, (len(revenue))):
        monthlyRev.append((int(revenue[x]) - int(revenue[x-1])))

    # Finds the average change in profit/loss over the entire period
    average = mean(monthlyRev)

    # Builds our dictionary with monthly revenue profit/loss
    for x in range(1, (len(month))):
        final[month[x]] = int(monthlyRev[x-1])

    # I don't fully understand what's going on here, it was the recommended answer on Stack Overflow
    # Functionally, it returns the largest and smallest values
    greatInc = max(zip(final.values(), final.keys()))
    greatDec = min(zip(final.values(), final.keys()))

    # Creates our read out for financial analysis
    analysis.append('Financial Analysis')
    analysis.append('----------------------------')
    analysis.append('Total Months: ' + str(totalMonth))
    analysis.append('Total Revenue: $' + str(totalRevenue))
    analysis.append('Average Revenue Change: $' + str(average))
    analysis.append('Greatest Increase in Revenue: ' + str(greatInc[1]) + ' ($' + str(greatInc[0]) + ')')
    analysis.append('Greatest Decrease in Revenue: ' + str(greatDec[1]) + ' ($' + str(greatDec[0]) + ')')

    # Prints analysis in terminal
    print("\n".join((analysis)))

# Writes our .txt output file
with open(output_file, 'w') as txtfile:
    txtfile.write('\n'.join(analysis))