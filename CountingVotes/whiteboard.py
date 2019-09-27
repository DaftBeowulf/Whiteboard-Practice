# Counting Votes
# You've been hired to write the software to count the votes for a local election.
# Write a function `countVotes` that receives an array of (unique) names, each one
# representing a vote for that person. Your function should return the name of the
# winner of the election. In the case of a tie, the person whose name comes last
# alphabetically wins the election (a dumb rule to be sure, but the voters don't
# need to know).

# Example:
# ```
# input: ['veronica', 'mary', 'alex', 'james', 'mary', 'michael', 'alex', 'michael'];

# expected output: 'michael'
# ```


def countVotes(votes):
    # create hash table for referencing names
    # create reference for highest vote count so far
    # iterate over each vote and increment entry in the table for that name
    # after final entry, return name of current highest vote holder
    tallies = {}
    leader = votes[0]  # set first entry as leader to be checked against
    for v in votes:
        if v in tallies:  # voted name already tracked, increment vote count
            tallies[v] += 1
        else:
            tallies[v] = 1  # track voted name, start count at 1
        if tallies[v] > tallies[leader] or (tallies[v] == tallies[leader] and v > leader):
            leader = v

    return leader


print(countVotes(['veronica', 'mary', 'alex', 'james', 'mary',
                  'michael', 'alex', 'michael']))  # should return 'Michael'
