import os, csv

# path to the election csv
csv_path = os.path.join('Resources', 'election_data.csv')

# opening and reading the csv file 
with open(csv_path, 'r') as csv_file:

    # splitting the data with commas 
    csv_reader = csv.reader(csv_file, delimiter=',')

    # skipping the header row
    next(csv_reader)

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

    # time to tally up the votes!
    for count in votes:
        index = unique_candidates.index(count)
        tally[index] += 1

    print(tally)
        

    
        
        
    

