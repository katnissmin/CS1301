"""
Georgia Institute of Technology - CS1301
HW08 - CSV Files/APIs
"""
import requests
#########################################
"""
Function Name: fallActivites() 
Parameters: fileName(str), interestedList(list), month(str), minimumRatio(float) 
Returns: greatestTupule(tuple) 
"""
def fallActivities(fileName, interestedList, month, minimumRatio):
    import csv
    with open(fileName, "r") as file:
        records = []
        dataline = csv.reader(file)
        for lines in dataline:
            records.append(lines)
        records.remove(records[0])

    activity = ""
    max = 0
    for i in range(0, len(records)):
        if records[i][0] in interestedList and records[i][3]== month:
            ratio = int(records[i][1])/int(records[i][2])
            #declare count
            count = 0
            if ratio > max:
                activity = records[i][0]
                count += 1
                max = ratio
        else:
            activity = activity

    if (minimumRatio > max) or (count > 1):
        return "No activities this month!"
    else:
        return (activity, max)



#########################################
"""
Function Name: funFallFavs() 
Parameters: fileName (str), letter (str) 
Returns: monthDict (dict) 
"""
def funFallFavs(fileName, letter):
    import csv
    with open(fileName, "r") as file:
        records = []
        dataline = csv.reader(file)
        for lines in dataline:
            records.append(lines)

    finalact = []
    for i in range(1, len(records)):
        if letter.lower() in records[i][0].lower():
            finalact.append(records[i][3])

    adict = {}
    for i in finalact:
        if i not in adict:
            adict[i] = 1
        else:
            adict[i] += 1

    if len(adict) == 0:
        return "Letter not found."
    else:
        return adict
#########################################
"""
Function Name: shareBorder() 
Parameters: country1 (str), country2 (str) 
Returns: areNeighbors (bool) 
"""
def shareBorder(country1, country2):
    data = (requests.get("https://restcountries.com/v2/all")).json()

    for i in data:
        if i["name"] == country2:
            abr = i["alpha3Code"]
            continue

    for i in data:
        if i["name"] == country1:
            if abr in i["borders"]:
                return True
            
    else:
        return False

"""
Function Name: currencyRatio() 
Parameters: continent (str), currency (str) 
Returns: ratio (float) 
"""
def currencyRatio(continent, currency):
    data = (requests.get("https://restcountries.com/v2/region/"+continent).json())

    count1 = len(data)

    count2 = 0
    for country in data:
        for currencyname in country["currencies"]:
            if currencyname["name"] == currency:
                count2 += 1
    
    answer = count2/count1
    
    return round(answer, 2)

#need to count how many countries are in the continent
#need to count how many countries in the continent use the given currency

#########################################
"""
Function Name: countriesInfo()
Parameters: countriesList (list)
Returns: None(NoneType)
"""
def countriesInfo(countriesList):
    file = open("countries.csv", "w")
    file.write("Country,Capital,Population,Languages,Currencies")

    for i in countriesList:
        data = (requests.get("https://restcountries.com/v2/name/"+i)).json()
        if type(data) == list:
            country = i
            capital = data[0]["capital"]
            population = data[0]["population"]
            languages = data[0]["languages"]
            lang = ""
            for j in languages:
                lang += j["name"]
                lang += "-"
            lang = lang.strip("-")
            currencies = data[0]["currencies"]
            money = ""
            for k in currencies:
                money += k["name"]
                money += "-"
            money = money.strip("-")
            tup2 = ("\n" + country + "," + capital + "," + str(population) + "," + lang + "," + money)
            file.write(tup2)
        else:
            continue

    file.close()


  

