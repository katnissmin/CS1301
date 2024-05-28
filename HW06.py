"""
Georgia Institute of Technology - CS1301
HW06 -  Dictionaries and Try/Except
"""
#########################################
"""
Function Name: dinnerTimer()
Parameters: meal (str), diningHalls (dict)
Returns: optionsList (list)
"""
def dinnerTime(meal, diningHalls):
    answer = []

    for key, value in diningHalls.items():
        for i in range(0, len(value)):
            if value[i] == meal:
                answer.append(key)

    if answer == []:
        return "Eat at home!"
    else:
        return answer

#########################################
"""
Function Name: rateActor()
Parameters: skillScore (list), fanScore (List)
Returns: totalScores (dict)
"""
def rateActor(skillScore, fanScore):
    name = []
    score_list = []
    score_list2 = []
    score = 0
    score2 = 0
    score3 = 0
    final = {}

    # try:
    for i in range(0, len(skillScore)):
        for j in range(0, 1):
            name.append(skillScore[i][0])

    for i in range(0, len(skillScore)):
        for j in range(0, 1):
            score = skillScore[i][1]

            try:
                if type(score) == int or type(score) == float:
                    score_list.append(score)
                else:
                    raise Exception
            except:
                score = 3
                score_list.append(score)

    for i in range(0, len(fanScore)):
        for j in range(0, 1):
            score2 = fanScore[i][1]

            try:
                if type(score) == int or type(score) == float:
                    score3 = score_list[i] + score2
                    score_list2.append(score3)
                else:
                    raise Exception
            except:
                score3 = score_list[i] + 3
                score_list2.append(score3)
    final = dict(zip(name, score_list2))

    return final

# skillScore = [("Harry Styles", 1), ("Florence Pugh", 5), ("Chris Pine", 4), ("Olivia Wilde", "%%%%")]
# fanScore = [("Harry Styles", 5), ("Florence Pugh", 5), ("Chris Pine", None), ("Olivia Wilde", 2)]
# print(rateActor(skillScore, fanScore))
#########################################
"""
Function Name: theRealDeal()
Parameters: stockDict (`dict`), goodStock (`str`)
Returns: richList (`list`)
"""
def theRealDeal(stockDict, goodStock):
    stockdata = list(stockDict.values())

    stockname = list(stockDict.keys())

    profitlist = []
    namelist = []
    goodEarning = 0.0

    for j in range(0, len(stockdata)):
        profit = stockdata[j][0] * stockdata[j][1] * stockdata[j][2]
        profitlist.append(profit)

    for i in range(0, len(stockname)):
        if profitlist[i] > 7000:
            namelist.append(stockname[i])

    namelist.sort()

    if goodStock in stockname:
        index = stockname.index(goodStock)
        profit = stockdata[index][0] * stockdata[index][1] * stockdata[index][2]
        namelist.insert(0, profit)
    else:
        statement = "You haven't invested in this one yet!"
        namelist.insert(0, statement)

    return namelist


# stockDict = {"LLY":(323.86, 10, 3.98), "ENPH":(277.47, 50, -0.72), "NBIX":(106.21, 100, 2.62)}
# goodStock = "LMD"
# print(theRealDeal(stockDict, goodStock))
#########################################
"""
Function Name: flightsInfo()
Parameters: flightsDict(`dict`)
Returns: fixedflightsDict(`dict`)
"""
#add an element to a tuple in a list in a dictionary in a dictionary
#go through each flight (loop through flightsDict) -> using a for loop #flightDict[flight]
#within the single flight, access the values of the passengers
#

def flightsInfo(flightsDict):
    for flight in flightsDict:
        i = flightsDict[flight]
        # i is the whole "flight1" or "flight2" dictionary
        info = i["passengers"]
        #info is the list which contains (name, seat, zone) or (name, seat)
        newlist = []
        # j is the tuple (n,s,z) or (n,s)
        for j in i["passengers"]:
            if len(j) == 2:
                newtuple = (j[0], j[1])
                if 0 <= len(j[0]) <= 5:
                    newtuple += ("A",)
                elif len(j[0]) == 6:
                    newtuple += ("B",)
                elif len(j[0]) >= 7:
                    newtuple += ("Premium",)
                newlist.append(newtuple)
            else: #don't have to do anything, just add the same tuple back to the list
                newlist.append(j)
            i["passengers"] = newlist

    return flightsDict


# print(flightsInfo({"flight1":
#                    {
#                     "time":"6:00am",
#                     "weather":"windy",
#                     "passengers": [("Farah","20A","A"), ("Jane","4A"),
#                                     ("Naomi", "3B"),("Fareeda", "1B","Premium'")]
#                    },
#                    "flight2":
#                    {
#                      "time":"3:00 pm",
#                      "weather":"sunny",
#                      "passengers": [("Nelson","2C"), ("Ramya","4A")]
#                    }
#                   }))
#########################################
"""
Function Name: fastFood()
Parameters: friendDict(`dict`), menu('dict')
Returns: friendsOwed(list)
"""
def fastFood(friendDict, menu):
    name = []
    friendfood = []
    fast = []
    cost = 0.0
    a = 0.0
    price = []
    hm = []
    sum = []
    menus = ()
    merged_list =[]

    name = list(friendDict.keys())

    friendfood = list(friendDict.values())

    for i in friendfood:
        print(i)
        total = 0.0
        for j in i:
            cost = menu.get(j)
            print(cost)
            total += cost
        sum.append(total)
    print(sum)

    merged_list = tuple(zip(name, sum))
    merged_list = list(merged_list)
    list.sort(merged_list)

    return merged_list

# friendDict = {
#     "Chris": ["coke", "cookie"],
#     "Andrew": ["fries", "burger"],
#     "Naomi": ["burger"]
# }
# menu = {
#     "coke": 1.0,
#     "fries": 3.0,
#     "burger": 10.0,
#     "cookie": 2.0
# }
# print(fastFood(friendDict, menu))

