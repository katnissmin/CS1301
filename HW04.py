"""
Georgia Institute of Technology - CS1301
HW03 -  Loops and Iteration
"""
#########################################
"""
Function Name: decodeString()
Parameters: encodedStr(str)
Returns: decodedList(list)
"""
def decodeString(encodedStr):
    newstring = encodedStr[::-1]
    newstring2 = newstring.replace("@", "")
    newstring3 = newstring2.lower()
    newstring4 = newstring3.split("#")
    return newstring4

#########################################
"""
Function Name: goodBrunch()
Parameters: ashList(list), nickList (list)
Returns: brunchDecision(list)
"""
def goodBrunch(ashList, nickList):
    ashList = set(ashList)
    nickList = set(nickList)

    if len(ashList & nickList) > 1:
        common = ashList & nickList
        common = list(common)
        return(sorted(common))
    if len(ashList & nickList) == 1:
        common1 = ashList & nickList
        common1 = ''.join(map(str,common1))
        return (common1)
    else:
        return("Brunch at home it is!")

#########################################
"""
Function Name: room_dist()
Parameters: dormMap (list), name1 (str), name2 (str)
Returns: distance (int)
"""
def room_dist(dormMap, name1, name2):
    length = len(dormMap)
    # print (length)
    location1 = 0
    location2 = 0
    for j in range(0, length):
        # print("hi")
        for k in range(0, 2):
            if (dormMap[j][k] == name1):
                location1 = j
            if (dormMap[j][k] == name2):
                location2 = j
            # print("hihi")
    distance = location1 - location2
    distance = abs(distance)
    # print (location1)
    # print (location2)
    return distance

#########################################
"""
Function Name: freshProduce()
Parameters: veggies (list), prices (list)
Returns: veggieList (list)
"""
def freshProduce(veggies, prices):
    total = 0.0
    afford = []
    length = len(veggies)
    for i in range(0, length):
        if prices[i] <= 4:
            afford.append(veggies[i])
            total += prices[i]
    afford.append(total)
    if total == 0.0:
        return []
    return afford

#########################################
"""
Function Name: find_roommate()
Parameters: my_interests(list), candidates (list), candidate_interests(list)
Returns: match (list)
"""

def find_roommate(my_interest, candidates, candidate_interests):
    me = len(my_interest)
    you = len(candidates)
    common = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    names = []
    for j in range(0, you):
        hobby = len(candidate_interests[j])
        count = 0
        for k in range(0, hobby):
            if candidate_interests[j][k] in my_interest:
                #common[j].append(candidate_interests[j][k])
                count += 1
        common[j] = count
    for l in range(0, len(common)):
        if common[l] >= 2:
            names.append(candidates[l])
    return names
