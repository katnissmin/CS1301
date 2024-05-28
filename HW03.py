"""
Georgia Institute of Technology - CS1301
HW03 -  Loops and Iteration
"""
#########################################
import math

"""
Function Name: product()
Parameters: nums(str)
Returns: product(int)
"""

def product(numbers):
    product = 1
    numbers = str(numbers)

    for i in numbers:
        product = product * int(i)

    return product

#########################################
"""
Function Name: recipeCount()
Parameters: recipe(str)
Returns: totalTeaspoons(int)
"""

def recipeCount(recipe):
    count = 0
    for c in recipe:
        if c.isdigit():
            count += int(c)
    return count

#########################################
"""
Function Name: instagraminator()
Parameters: usernames(str)
Returns: decodedUsernames(str)
"""

#def instagraminator(usernames):
    #decodedUsernames = ' '.join(filter(str.isalnum, usernames))
    #return decodedUsernames

def instagraminator(usernames):
    decodedUsernames = ''
    for c in usernames:
        if c != "@" and c != "_" and c != "$":
            decodedUsernames += c
    return decodedUsernames

#########################################
"""
Function Name: studentLoans()
Parameters: loanAmount(int)
Returns: forgivenessCount(int)
"""

def studentLoans(loanAmount):
    forgivenessCount = 0
    while loanAmount > 0:
        loanAmount -= 10000
        forgivenessCount += 1
    return forgivenessCount

#########################################
"""
Function Name: playoffs()
Parameters: team1name (str), team2name (str), scoreCount (str) 
Returns: winningTeam (str) 
"""

def playoffs(team1name, team2name, scoreCount):
    team1 = 0
    team2 = 0

    for c in scoreCount:
        if c == "1":
            team1 += 1
        if c == "2":
            team2 += 1

    if team1 > team2:
        return(team1name + " has won the game!")
    elif team1 < team2:
        return(team2name + " has won the game!")
    else:
        return("It was a tie :(")


