# Programmer : Alexander Walker
# Description : This program grabs a list of 1000 ages from a file, then checks to see which ones can and cannot vote.

#Counters that add a point for every person that can vote and cannot vote.
voter = 0
non_voter = 0

# Read a list of ages from a file into the variable ages.
ages_file = open("ages.txt")
ages = [int(age) for age in ages_file]
ages_file.close()

#For loop that prints and checks for people who can and can't vote.
for age in ages:
    
    if (age >= 18):
        voter += 1
    
    else:
        non_voter += 1

#Prints how many voters there are.
print(f"Voters: {voter}")

#Prints how many non voters there are.
print(f"Non-voters: {non_voter}")