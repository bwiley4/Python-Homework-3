import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

counts = []
candidate_list = []
vote_counts = []
percentage = []






with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        counts.append(row[0])
        candidate_list.append(row[2])
    vote = (len(counts))
    print("Election Results")
    print("---------------")
    print(f'Total Votes: {vote}')

    # i = csv_header[2]
    
    # if i in candidate_list:
    #     candidate = candidate_list.index(i)
    #     vote_counts[candidate] = vote_counts[candidate] + 1
    # else:
    #     candidate_list.append(i)
    #     vote_counts.append(1)

    Khan = int(candidate_list.count("Khan"))
    Correy = int(candidate_list.count("Correy"))
    Li = int(candidate_list.count("Li"))
    O_Tooley = int(candidate_list.count("O'Tooley"))

    khan_vote_per = (Khan/vote) * 100
    correy_vote_per = (Correy/vote) * 100
    Li_vote_per = (Li/vote) * 100
    tooley_vote_per = (O_Tooley/vote) * 100


    
    
    
    
    print(f'Khan: {khan_vote_per, Khan}')
    print(f'Correy: {correy_vote_per, Correy}')
    print(f'Li: {Li_vote_per, Li}')
    print(f"O'Tooley: {tooley_vote_per, O_Tooley}")
    print(f'Winner:Khan')
    
    output_file = os.path.join("Election_Results.txt")