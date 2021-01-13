import os, csv

# path to the election csv
csv_path = os.path.join('Resources', 'election_data.csv')

# opening and reading the csv file 
with open(csv_path, 'r') as csv_file:

    # splitting the data with commas 
    csv_reader = csv.reader(csv_file, delimiter=',')

    # storing/skipping the header row
    csv_header = next(csv_reader)

    # creating my lists 
    votes = []
    candidates =[]
    unique_candidates = []
    tally = []
    
    # collecting all votes
    for row in csv_reader:
        votes.append(row[2])

    # capturing all unique candidates
    candidates = set(votes)
    unique_candidates = list(candidates)

    # setting up my vote counter
    for count in range(len(unique_candidates)): 
        tally.append(0)

    # counting total votes 
    totVotes = len(votes)

    # time to tally up the votes!
    for count in votes:
        index = unique_candidates.index(count)
        tally[index] += 1

    max_votes = max(tally)

# creating the results summary, outputing the results into a text file, as well as the terminal
output_path = os.path.join("Analysis", "Election_Results.txt")
with open(output_path, 'w', newline='') as textfile:

    textfile.write("Election Results\n")
    textfile.write("--.---------------.---------------.----------\n\n")

    print("Election Results")
    print("--.---------------.---------------.----------")
    
    # building a list of tuples to create the relationship between candidates and their votes, 
    # then sorting the tuples in descending order by number of votes

    election_results = sorted(list(zip(tally, unique_candidates)), reverse = True)
    for index in range(len(election_results)):
        if election_results[index][0] == max_votes:
            winner = election_results[index][1]
        textfile.write(f" {election_results[index][1]}: {(election_results[index][0]/totVotes * 100): .3f}% ({election_results[index][0]}) \n")
        print(f" {election_results[index][1]}: {(election_results[index][0]/totVotes * 100.000): .3f}% ({election_results[index][0]}) ")

    textfile.write("\n--.---------------.---------------.----------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("--.---------------.---------------.----------\n")

    print("--.---------------.---------------.----------")
    print(f"Winner: {winner}")
    print("--.---------------.---------------.----------")
