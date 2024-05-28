"""
Georgia Institute of Technology - CS1301
HW05 -  Lists, Tuples, and Modules
"""
#########################################
"""
Function Name: teamPicker()
Parameters: sportInterests (list), intramural (str)
Returns: team (list)
"""

# need to access the list in the tuple in a list
# if there is a common sport in the list, index the name of the friend
# in the tuple
# and print the list of names

def teamPicker(sportInterests, intramural):
    common = [item[1] for item in sportInterests]
    name = [item[0] for item in sportInterests]
    team =[]
    for i in range(0, len(common)):
        if intramural in common[i]:
            team.append(name[i])
    if len(team) != 0:
        return sorted(team)
    else:
        return ("Free agent :/")

#########################################
"""
Function Name: vacationPlanner()
Parameters: trips (list), costs (list)
Returns: vacationSpots (tuple)
"""
# return a tuple with the cheapest country in ALPHABETICAL ORDER
# and a list of tuples which match the trip and the cost
# in ALPHABETICAL ORDER
# need to return a tuple?

def vacationPlanner(trips, costs):
    if trips == [] or costs == []:
        return ("", [])

    minPrice = min(costs)
    list1 = []
    i = 0

    for i in range(0, len(costs)):
        if costs[i] == minPrice:
            list1.append(trips[i])

    list2 = sorted(list1)

    list3 = sorted(trips)
    list4 = []
    i = 0

    for i in range(0, len(costs)):
        list4.append((list3[i], costs[trips.index(list3[i])]))

    list2.append(list4)
    return tuple(list2)


#########################################
"""
Function Name: fastFood()
Parameters: foods (list), costs (list)
Returns: friendsOwed (list)
"""

# name -> food -> price
# result: name, price
# need to index name and match with food with price
# use enumerate(tuple)?
###enumerate gives you (index, value)
###the item in right side of the tuple is the value
#enumerate the tuple and then list it (enumerate gives you the index)
#adding a value with list.append() (convert the tuple to a list and then add an object)

#list of names in order
#search costs() for the name
#take in the cost for every time it appears
#name[1] will connect with costs[1]

def fastFood(foods, costs):
    name = []
    friendfood = []
    fast = []
    price = []

    namelist = []
    money = []
    new_namelist = []
    new_money = []
    o = 0.0

    merged_list = []
    merged_list2 = []

    for i in range(len(foods)):
        for j in range(0, 1):
            name.append(foods[i][0])
            friendfood.append(foods[i][1])

    for k in range(len(costs)):
        for l in range(0, 1):
            fast.append(costs[k][0])
            price.append(costs[k][1])

#if the name repeats in "name", need to add the cost together
#if a is in the list, make it the value and look again, add the new value
#get rid of the name which is being duplicated

    for m in range(0, len(foods)):
        namelist.append(name[m])
        p = fast.index(friendfood[m])
        o = 0.0 + price[p]
        money.append(o)

    merged_list = tuple(zip(namelist, money))
    merged_list = list(merged_list)
    list.sort(merged_list)

    for n in range(0, len(merged_list)):
        for p in range(0, 1):
            if merged_list[n][0] not in new_namelist:
                new_namelist.append(merged_list[n][0])
                new_money.append(merged_list[n][1])
                # print(new_namelist)
                # print(new_money)
            else:
                del new_namelist[-1]
                q = float(new_money[-1]) + float(merged_list[n][1])
                new_money.append(q)
                del new_money[-2]
                new_namelist.append(merged_list[n][0])
                # print(new_namelist)
                # print(new_money)

    merged_list2 = tuple(zip(new_namelist, new_money))
    merged_list2 = list(merged_list2)
    list.sort(merged_list2)

    return merged_list2

# def fastFood(foods, costs):
#     name = []
#     friendfood = []
#     fast = []
#     price = []
#     total = []
#     menu = ()
#     merged_list =[]
#
#     for i in range(len(foods)):
#         for j in range(0, 1):
#             name.append(foods[i][0])
#             friendfood.append(foods[i][1])
#
#     for m in range(len(costs)):
#         for n in range(0, 1):
#             fast.append(costs[m][0])
#             price.append(costs[m][1])
#
#     menu = dict((x, y) for x, y in costs)
#
#     for k in range(len(friendfood)):
#         if friendfood[k] in menu:
#             total.append(menu[friendfood[k]])
#
#     merged_list = tuple(zip(name, total))
#     merged_list = list(merged_list)
#     list.sort(merged_list)
#
#     return merged_list

#########################################
"""
Function Name: reviewSession()
Parameters: rooms (list), dates (list)
Returns: roomsAvailable (list)
"""
import calendar

def reviewSession(rooms, dates):
    month = []
    days = []
    list(dates)
    dayofweek = []
    answer = []

    for i in range (0, len(dates)):
        for j in range(0, 1):
            month.append(dates[i][0])
            days.append(dates[i][1])

    for k in range(0, len(month)):
        dayofweek.append(calendar.weekday(2022, month[k], days[k]))

    for l in range(0, len(dayofweek)):
        if dayofweek[l] == 3 or dayofweek[l] == 4:
            answer.append(rooms[l])

        else:
            answer

    res = [*set(answer)]
    res.sort()
    return res

# rooms = ['CULC 144', 'CULC 152', 'CCB 016', 'Skiles 246']
# dates = [(9,30), (10,1), (10,22), (10,21)]
# print(reviewSession(rooms, dates))

#########################################
"""
Function Name: esportsBracket()
Parameters: tourneyList (list)
Returns: tourneyWinner (str)
"""
from esportsMatch import matchHistory

def esportsBracket(tourneyList):

    finals = []
    finalWinner = []

    for i in range(0, len(tourneyList)):
        for j in range(0, 1):
            winner1 = matchHistory(tourneyList[0][0], tourneyList[0][1])
            finals.append(winner1)
            winner2 = matchHistory(tourneyList[1][0], tourneyList[1][1])
            finals.append(winner2)

    tourneyWinner = matchHistory(finals[0], finals[1])

    return tourneyWinner
