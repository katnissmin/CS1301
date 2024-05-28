"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
"""

#########################################

"""
Function Name: availableDate()
Parameters: date(int), isWeekend(bool)
Returns: availability(str)
"""

def availableDate(date, isWeekend):

    if date % 2 == 0 or isWeekend == True:
        return("Available on {}!".format(date))
    else:
        return("Not available :(")

#########################################

"""
Function Name: buyGame()
Parameters: gameTitle(str), budget(float), cost(float), positiveRating(float)
Returns: None(NoneType)
"""

def buyGame(gameTitle, budget, cost, positiveRating):

    if cost > budget:
        print("{} is over ${}!".format(gameTitle, budget))
    if cost < budget and positiveRating >= 0.7:
        print("Sasuke will buy {}!".format(gameTitle))
    if cost < budget and positiveRating < 0.7:
        print("Let's find another game.")

#########################################

"""
Function Name: foodTime()
Parameters: restaurant(str), time(int)
Returns: howLong(float or int)
"""

def foodTime(restaurant, time):
    if restaurant == "Cafe Leblanc" and (time - (10+5+2*(620/80)))>=0:
        return (time - (10+5+2*(620/80)))
    elif restaurant == "The Roost" and (time - (10+10+2*(700/80)))>=0:
        return (time - (10+10+2*(700/80)))
    elif restaurant == "Lumpy Pumpkin" and (time - (10+12+2*(850/80)))>=0:
        return (time - (10+12+2*(850/80)))
    elif restaurant == "The Milk Bar" and (time - (10+3+2*(1200/80)))>=0:
        return (time - (10+3+2*(1200/80)))
    else:
        return -1

#########################################

"""
Function Name: restaurantReservation()
Parameters: total(int), toSave(int), average(int)
Returns: canReserve(bool)
"""

def restaurantReservation(total, toSave, average):
    return (total > toSave+average*2)
    # if total > toSave+average*2:
    #     return True
    # if total < toSave+average*2:
    #     return False

#########################################

"""
Function Name: halloweenHeist()
Parameters: num1(int), num2(int), name(str)
Returns: message(str)
"""

def halloweenHeist(num1, num2, name):

    if num1-num2 > 0:
        return(name + " has the package.")
    elif num1-num2 < 0:
        return("{} does not have the package.". format(name))
    else:
        return("{} has taken over.".format(name))
