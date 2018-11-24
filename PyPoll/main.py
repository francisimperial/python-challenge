import os
import csv

election_csv = os.path.join('..', 'Resources', 'election_data.csv')

total_vote = 0
khan_vote = 0
correy_vote = 0
li_vote = 0
otooley_vote = 0

with open(election_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total_vote += 1

        if row[2] == "Khan":
            khan_vote += 1
        elif row[2] == "Correy":
            correy_vote += 1
        elif row[2] == "Li":
            li_vote += 1
        else:
            otooley_vote += 1

    if max([khan_vote, correy_vote, li_vote, otooley_vote]) == khan_vote:
        winner = "Khan"
    elif max([khan_vote, correy_vote, li_vote, otooley_vote]) == correy_vote:
        winner = "Correy"
    elif max([khan_vote, correy_vote, li_vote, otooley_vote]) == li_vote:
        winner = "Li"
    else:
        winner = "O'Tooley"

    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {total_vote}")
    print(f"-------------------------")
    print(f"Khan: {(khan_vote/total_vote *100):.3f}% ({khan_vote})")
    print(f"Correy: {(correy_vote/total_vote *100):.3f}% ({correy_vote})")
    print(f"Li: {(li_vote/total_vote *100):.3f}% ({li_vote})")
    print(f"O'Tooley: {(otooley_vote/total_vote *100):.3f}% ({otooley_vote})")
    print(f"-------------------------")
    print(f"Winner: {winner}")
    print(f"-------------------------")

    output_csv = os.path.join("election_results.csv")

    with open(output_csv, 'w') as file:
        file.write(f"Election Results\n")
        file.write(f"-------------------------\n")
        file.write(f"Total Votes: {total_vote}\n")
        file.write(f"-------------------------\n")
        file.write(f"Khan: {(khan_vote/total_vote *100):.3f}% ({khan_vote})\n")
        file.write(f"Correy: {(correy_vote/total_vote *100):.3f}% ({correy_vote})\n")
        file.write(f"Li: {(li_vote/total_vote *100):.3f}% ({li_vote})\n")
        file.write(f"O'Tooley: {(otooley_vote/total_vote *100):.3f}% ({otooley_vote})\n")
        file.write(f"-------------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write(f"-------------------------\n")
