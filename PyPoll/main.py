import csv
import os
from collections import Counter

csvpath = os.path.join('resources', 'election_data.csv')
output_file = os.path.join('resources', 'Election_Results.txt')

with open(csvpath, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Defines our lists
    candidates = []
    votePercentage = []
    results = []

    # I did not know there was Counter() class that streamlined what I aimed to do
    # I was originally working with convoluted for-loops with row[2] == or != name
    votesCounted = Counter()

    # Builds our list of candidates
    for row in csvreader:
        candidates.append(row[2])

    # The length in our list is the total number of votes
    totalVotes = len(candidates)

    # Tallying function for each candidate
    for name in candidates:
        votesCounted[name] += 1

    # Returns the candidate with the largest total votes
    winner = max(zip(votesCounted.values(), votesCounted.keys()))

    names = tuple(votesCounted.keys())
    votes = tuple(votesCounted.values())

    # Builds our list with percentages
    for x in votes:
        votePercentage.append((int(x)/totalVotes)*100)
    
    # Creates our read out for election results
    results.append('Election Results')
    results.append('-----------------------')
    results.append('Total Votes: ' + str(totalVotes))
    results.append('-----------------------')
    for x in range(len(names)):
        results.append(names[x] + ': ' + str(votePercentage[x]) + '% ' + '(' + str(votes[x]) + ')')
    results.append('-----------------------')
    results.append('Winner: ' + winner[1])
    results.append('-----------------------')

    # Prints results in terminal
    print("\n".join((results)))

# Writes our .txt output file
with open(output_file, 'w') as txtfile:
    txtfile.write('\n'.join(results))